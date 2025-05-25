from django.shortcuts import render

# Create your views here.
def resume_home(request):
    """
    Render the home page of the resume application.
    """
    return render(request, 'resume/resume_home.html')