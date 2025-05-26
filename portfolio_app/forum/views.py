from django.shortcuts import render

# Create your views here.
def forum(request):
    """
    Render the home page of the forum application.
    """
    return render(request, 'forum.html')