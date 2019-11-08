import os

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
from .models import *
from .forms import *
# Create your views here.


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    requirements = Requirement.objects.filter(project=project)
    specifications = []  # Specification.objects.filter()
    feedback = Feedback.objects.filter(project=project)
    concepts = Concept.objects.filter(project=project)
    for req in requirements:
        specs = Specification.objects.filter(requirements__id=req.id)
        for spec in specs:
            specifications.append({
                'id': spec.id,
                'description': spec.description,
                'value_type': spec.get_value_type_display,
                'goal_value': spec.goal_value,
                'requirements': spec.requirements.all(),
            })

    return render(request, 'projects/project.html', {'project': project, 'requirements': requirements, 'specifications': specifications, 'feedback': feedback, 'concepts': concepts})


def add_project(request):
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project', id=project.id)
    else:
        form = AddProjectForm()

    return render(request, 'projects/add_project.html', {'form': form})


def add_requirement(request):
    if request.method == "POST":
        form = AddRequirementForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project', id=project.id)
    else:
        form = AddRequirementForm()

    return render(request, 'projects/add_project.html', {'form': form})


def download_media(request, path):
    path = "projects/" + path
    MR = settings.MEDIA_ROOT
    file_path = MR + path
    print(file_path)
    print(settings.MEDIA_ROOT)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
