from django.shortcuts import render
from resume.models import Education, Experience, Skill
# Create your views here.
def resume(request):
    """
    Render the home page of the resume application.
    """
    context = {
        'educations': Education.objects.all(),
        'experiences': Experience.objects.all(),
        'skills': Skill.objects.all(),
    }

    return render(request, 'resume.html', context=context)