from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm


def accounts_profile(request, username):
    """
    Render the user profile page.
    """
    user = get_object_or_404(CustomUser, username=username)
    posts = user.get_posts().order_by('-created_at')[:5]  # Get the latest 5 posts
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'accounts/profile.html', context=context)


@login_required
def edit_profile(request, username):
    if request.user.username != username:
        return redirect('accounts:profile', username=request.user.username)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', username=request.user.username)
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})