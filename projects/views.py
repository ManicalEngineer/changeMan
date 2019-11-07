from django.shortcuts import render, get_object_or_404

from .models import *

# Create your views here.


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    requirements = Requirement.objects.filter(project=project)
    specifications = Specification.objects.filter(requirements__description__contains=requirements)
    # for req in requirements:
    #     specifications.append(Specification.objects.filter(requirements__id=req.id))

    print(specifications)
    return render(request, 'projects/project.html', {'project': project, 'requirements': requirements, 'specifications': specifications})
