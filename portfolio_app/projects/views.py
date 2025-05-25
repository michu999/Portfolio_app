from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page of the portfolio application.
    """
    return render(request, 'base.html')

def project_list(request):
    """
    Render the list of projects.
    """
    return render(request, 'projects/project_list.html')