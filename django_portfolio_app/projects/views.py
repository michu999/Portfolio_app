from django.shortcuts import render
from projects.models import Project, Technology

def projects(request):
    """
    Render the list of projects.
    """
    context = {
        'projects': Project.objects.all(),
        'technologies': Technology.objects.all(),
    }
    return render(request, 'projects.html', context=context)