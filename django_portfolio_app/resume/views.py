from django.shortcuts import render
from resume.models import Education, Experience, Skill, RelevantCourse, Language, ProjectSection, ContactInfo, Summary, Hobby
from projects.models import Project

def resume(request):
    """
    Render the home page of the resume application.
    """
    project_section = ProjectSection.objects.first()

    # Get projects either from ProjectSection or fallback to all projects
    projects = []
    if project_section and project_section.projects.exists():
        projects = project_section.projects.all()
    else:
        projects = Project.objects.all()

    context = {
        'education': Education.objects.all(),
        'experience': Experience.objects.all(),
        'skill': Skill.objects.all(),
        'relevant_course': RelevantCourse.objects.all(),
        'language': Language.objects.all(),
        'project_section': project_section,
        'projects': projects,
        'contact_info': ContactInfo.objects.first(),
        'summary': Summary.objects.first(),
        'hobbies': Hobby.objects.all(),
    }

    return render(request, 'resume.html', context=context)