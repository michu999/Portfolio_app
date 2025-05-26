from django.shortcuts import render
from forum.models import Post, Comment, Reaction, ReactionType

# Create your views here.
def forum(request):
    """
    Render the home page of the forum application.
    """
    # This view can be extended to include logic for displaying posts, comments, etc.
    # For now, it simply renders the 'forum.html' template.
    # You can pass context data to the template if needed.
    # Example context data (can be removed if not needed):
    context = {
        'posts': Post.objects.all(),
        'comments': Comment.objects.all(),
        'reactions': Reaction.objects.all(),
        'reaction_types': ReactionType.objects.all(),
        }
    #  # Render the template with the context data
    # return render(request, 'forum.html', context)
    return render(request, 'forum.html', context=context)