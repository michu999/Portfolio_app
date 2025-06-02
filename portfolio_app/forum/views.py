from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment, Reaction, ReactionType
from .forms import CommentForm
# Create your views here.
def forum(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum.html', {
        'posts': posts
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).prefetch_related('replies', 'author')

    # Count reactions for the post
    like_count = Reaction.objects.filter(post=post, reaction_type__name='Like').count()
    dislike_count = Reaction.objects.filter(post=post, reaction_type__name='Dislike').count()

    # Get and annotate comments with reaction counts
    for comment in comments:
        comment.like_count = Reaction.objects.filter(comment=comment, reaction_type__name='Like').count()
        comment.dislike_count = Reaction.objects.filter(comment=comment, reaction_type__name='Dislike').count()

        # Also count reactions for replies
        for reply in comment.replies.all():
            reply.like_count = Reaction.objects.filter(comment=reply, reaction_type__name='Like').count()
            reply.dislike_count = Reaction.objects.filter(comment=reply, reaction_type__name='Dislike').count()

    # Get user reactions if authenticated
    user_reaction = None
    if request.user.is_authenticated:
        user_reaction = Reaction.objects.filter(
            user=request.user,
            post=post
        ).select_related('reaction_type').first()

        # Get reactions to comments
        comment_reactions = Reaction.objects.filter(
            user=request.user,
            comment__in=[c.id for c in comments]
        ).select_related('reaction_type')

        comment_reaction_dict = {r.comment_id: r for r in comment_reactions}
        for comment in comments:
            comment.user_reaction = comment_reaction_dict.get(comment.id)

            for reply in comment.replies.all():
                reply.user_reaction = comment_reaction_dict.get(reply.id)

    # Create comment form
    comment_form = CommentForm()

    return render(request, 'forum/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user_reaction': user_reaction,
        'like_count': like_count,
        'dislike_count': dislike_count,
    })

@login_required
def add_post(request):
    """Add a new post to the forum"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not title or not content:
            return JsonResponse({'success': False, 'error': 'Title and content are required'}, status=400)

        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )

        return redirect('forum:post_detail', post_id=post.id)

    # Handle GET request by rendering the form
    return render(request, 'forum/add_post.html', {
        'title': 'New Post'
    })

@login_required
@require_POST
def add_comment(request, post_id, parent_id=None):
    """Add a comment to a post or another comment"""
    post = get_object_or_404(Post, id=post_id)
    parent = None

    if parent_id:
        parent = get_object_or_404(Comment, id=parent_id, post=post)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.parent = parent
        comment.save()

        # If this is an AJAX request, return JSON response
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'comment_id': comment.id,
                'author': comment.author.username,
                'content': comment.content,
                'created_at': comment.created_at.strftime('%B %d, %Y %H:%M'),
            })

        # Otherwise redirect back to the post
        return redirect('forum:post_detail', post_id=post.id)

    # If form is invalid
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    # For non-AJAX requests, redirect back with errors
    return redirect('forum:post_detail', post_id=post.id)


@login_required
@require_POST
def toggle_reaction(request):
    """Toggle a reaction (like/dislike) on a post or comment"""
    post_id = request.POST.get('post_id')
    comment_id = request.POST.get('comment_id')
    reaction_type_name = request.POST.get('reaction_type')

    # Validate reaction type (only allow Like/Dislike)
    if reaction_type_name not in ['Like', 'Dislike']:
        return JsonResponse({'success': False, 'error': 'Invalid reaction type'}, status=400)

    try:
        reaction_type = ReactionType.objects.get(name=reaction_type_name)
    except ReactionType.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Reaction type not found'}, status=404)

    if post_id:
        post = get_object_or_404(Post, id=post_id)
        # Check if user already reacted to this post
        existing_reaction = Reaction.objects.filter(
            user=request.user,
            post=post,
            comment__isnull=True
        ).first()

        if existing_reaction:
            if existing_reaction.reaction_type == reaction_type:
                # Toggle off same reaction
                existing_reaction.delete()
                action = 'removed'
            else:
                # Change reaction type
                existing_reaction.reaction_type = reaction_type
                existing_reaction.save()
                action = 'changed'
        else:
            # Create new reaction
            Reaction.objects.create(
                user=request.user,
                reaction_type=reaction_type,
                post=post
            )
            action = 'added'

        # Count reactions
        like_count = Reaction.objects.filter(post=post, reaction_type__name='Like').count()
        dislike_count = Reaction.objects.filter(post=post, reaction_type__name='Dislike').count()

        return JsonResponse({
            'success': True,
            'action': action,
            'like_count': like_count,
            'dislike_count': dislike_count,
            'target_type': 'post',
            'target_id': post_id,
            'reaction_type': reaction_type_name
        })

    elif comment_id:
        comment = get_object_or_404(Comment, id=comment_id)
        # Check if user already reacted to this comment
        existing_reaction = Reaction.objects.filter(
            user=request.user,
            comment=comment,
            post__isnull=True
        ).first()

        if existing_reaction:
            if existing_reaction.reaction_type == reaction_type:
                # Toggle off same reaction
                existing_reaction.delete()
                action = 'removed'
            else:
                # Change reaction type
                existing_reaction.reaction_type = reaction_type
                existing_reaction.save()
                action = 'changed'
        else:
            # Create new reaction
            Reaction.objects.create(
                user=request.user,
                reaction_type=reaction_type,
                comment=comment
            )
            action = 'added'

        # Count reactions
        like_count = Reaction.objects.filter(comment=comment, reaction_type__name='Like').count()
        dislike_count = Reaction.objects.filter(comment=comment, reaction_type__name='Dislike').count()

        return JsonResponse({
            'success': True,
            'action': action,
            'like_count': like_count,
            'dislike_count': dislike_count,
            'target_type': 'comment',
            'target_id': comment_id,
            'reaction_type': reaction_type_name
        })

    return JsonResponse({'success': False, 'error': 'No post or comment specified'}, status=400)