from django.shortcuts import render

def projects(request):
    """
    Render the list of projects.
    """
    return render(request, 'projects.html')