from django.shortcuts import render

# Create your views here.
def resume(request):
    """
    Render the home page of the resume application.
    """
    return render(request, 'resume.html')