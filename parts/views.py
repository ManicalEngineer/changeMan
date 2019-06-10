from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Part
from changes.models import Revision, ECO, ECR
from .forms import AddPartForm

# Create your views here.


def add_part(request):

    if request.method == "POST":
        form = AddPartForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            part.initiated_by = request.user
            part = form.save()
            return redirect('part_summary', part_number=part.part_number)
    else:
        form = AddPartForm()

    return render(request, 'parts/add_part.html', {'form': form})


def part(request, part_number):
    part = Part.objects.get(pk=part_number)
    revs = Revision.objects.filter(revised_drawing=str(part_number))
    ecos = ECO.objects.filter(part_numbers=str(part_number))
    ecrs = ECR.objects.filter(part_numbers=str(part_number))
    return render(request, 'parts/part_detail.html', {'part': part, 'revs': revs, 'ecos': ecos, 'ecrs': ecrs})
