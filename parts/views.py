from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.templatetags.static import static
from django.conf import settings
from datetime import date

from .models import Part
from changes.models import Revision, ECR
from .forms import AddPartForm

import json
import os

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


def part(request):
    part_number = request.GET.get("part")
    part = Part.objects.get(pk=part_number)
    revs = Revision.objects.filter(revised_drawing=str(part_number))
    ecrs = ECR.objects.filter(part_numbers=str(part_number))
    return render(request, 'parts/part_detail.html', {'part': part, 'revs': revs, 'ecrs': ecrs})


def get_last(request):
    partial_pn = request.POST.get("part_number", "")

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

        part = partial_pn + last_three
        print(partial_pn)
        print(part)

    else:

        part = partial_pn + "000"

    return HttpResponse(part)


def part_list(request):
    parts = Part.objects.all().order_by('part_number')
    # deleteThis = Part.objects.get(part_number="O/H LINE EXT 8 FT")
    # print(deleteThis)
    # deleteThis.delete()

    return render(request, 'parts/part_list.html', {'parts': parts})


def updateSeries(request):

    if request.method == "POST":
        pn_dict = json.loads(request.body)
        print(json.dumps(pn_dict, indent=4, sort_keys=True))
        today = date.today()
        dateStr = today.strftime("%d%b%y")
        JSON_PATH = settings.STATICFILES_DIRS[0] + '\\javascript\\part_number_data.json'
        NEW_JSON_PATH = settings.STATICFILES_DIRS[0] + '\\javascript\\part_number_data' + dateStr + '.json'
        i = 0
        while os.path.exists(NEW_JSON_PATH):
            NEW_JSON_PATH = settings.STATICFILES_DIRS[0] + '\\javascript\\part_number_data-' + dateStr + '-' + str(i) + '.json'
            i = i + 1

        os.rename(JSON_PATH, NEW_JSON_PATH)
        with open(JSON_PATH, 'w') as pn_json:
            json.dump(pn_dict, pn_json)

        return HttpResponse("OK")

    return render(request, 'parts/add_series.html')


def edit_part(request, part_number):

    part = Part.objects.get(pk=part_number)
    if request.method == "POST":
        form = AddPartForm(request.POST, instance=part)
        if form.is_valid():
            part = form.save()
            return redirect('part_summary', part_number=part.part_number)
    else:
        form = AddPartForm(instance=part)
    return render(request, "parts/add_part.html", {'form': form})
