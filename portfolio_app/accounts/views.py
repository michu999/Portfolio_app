from django.shortcuts import render

# Create your views here.
def accounts_profile(request):
    """
    Render the user profile page.
    """
    return render(request, 'accounts/profile.html')
