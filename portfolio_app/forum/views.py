from django.shortcuts import render

# Create your views here.
def forum_home(request):
    """
    Render the home page of the forum application.
    """
    return render(request, 'forum/forum_home.html')