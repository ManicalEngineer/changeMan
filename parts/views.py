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

def get_last(request):
    partial_pn = request.POST.get("part_number","")
    
    p = Part.objects.filter(part_number__contains=partial_pn).last()

    if p is not None:
        
        part = p.part_number

        if part[-3:] != '000':
            
            last_three = part[-3:].lstrip('0')

            last_three = str(int(last_three) + 1)

        else:
            
            last_three = "1"

        while len(last_three) < 3:
            last_three = "0" + last_three

        part = part[:8] + last_three

    else:

        part = partial_pn + "-000"

    return HttpResponse(part)
