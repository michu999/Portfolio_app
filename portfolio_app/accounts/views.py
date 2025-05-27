from django.shortcuts import render

# Create your views here.
def accounts_profile(request):
    """
    Render the user profile page.
    """
    return render(request, 'account/profile.html')

def user_login(request):
    """
    Render the user login page.
    """
    return render(request, 'account/login.html')

def user_logout(request):
    """
    Render the user logout page.
    """
    return render(request, 'account/logout.html')