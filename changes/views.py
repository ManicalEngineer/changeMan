from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from datetime import timedelta

from .models import ECO, ECR
from parts.models import Part
from .forms import AddECRForm, AddECOForm, CreateRevision

# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        ecrs = ECR.objects.filter(engineer__exact=request.user)
        ecos = ECO.objects.filter(engineer__exact=request.user)
        parts = Part.objects.filter(initiated_by__exact=request.user)
        return render(request, 'changes/dashboard.html', {'ecrs': ecrs, 'ecos': ecos, 'parts': parts})
    else:
        return render(request, 'redirect.html')


def ecr_list(request):
    op_ecrs = ECR.objects.filter(status__exact='OP')
    ip_ecrs = ECR.objects.filter(status__exact='IP')
    oh_ecrs = ECR.objects.filter(status__exact='OH')
    return render(request, 'changes/ecr_list.html', {'op_ecrs': op_ecrs, 'ip_ecrs': ip_ecrs, 'oh_ecrs': oh_ecrs})


def ecr_detail(request, ecr_number):
    ecr = get_object_or_404(ECR, pk=ecr_number)
    mf = ECR._meta.get_fields()
    return render(request, 'changes/ecr_detail.html', {'ecr': ecr, 'mf': mf})


def ecr_add(request):
    if request.method == "POST":
        form = AddECRForm(request.POST)
        if form.is_valid():
            ecr = form.save(commit=False)
            ecr.initiated_by = request.user

            if ecr.priority == '1':
                ecr.deadline = ecr.create_date + timedelta(weeks=1)
            elif ecr.priority == '2':
                ecr.deadline = ecr.create_date + timedelta(weeks=2)
            else:
                ecr.deadline = ecr.create_date + timedelta(months=3)

            ecr = form.save()
            return redirect('ecr_detail', ecr_number=ecr.ECR_number)
    else:
        form = AddECRForm()

    return render(request, 'changes/add_ecr.html', {'form': form})


def ecr_edit(request, ecr_number):
    ecr = ECR.objects.get(pk=ecr_number)
    if request.method == "POST":
        form = AddECRForm(request.POST, instance=ecr)
        if form.is_valid():
            ecr = form.save()
            ecr.initiated_by = request.user

            if ecr.priority == '1':
                ecr.deadline = datetime.now() + timedelta(days=3)
                ecr.save()
            elif ecr.priority == '2':
                ecr.deadline = datetime.now() + timedelta(weeks=2)
                ecr.save()
            else:
                ecr.deadline = datetime.now() + timedelta(months=3)
                ecr.save()

            if ecr.status == 'CL' and ecr.ecr_disposition == 'ECO':
                ecr = form.save()
                eco = ECO()
                ecr.close_date = datetime.now()
                eco.eco_title = ecr.ecr_title
                eco.ECR_number = ecr
                eco.save()
                eco.deadline = ecr.deadline
                eco.part_numbers.set(ecr.part_numbers.all())
                eco.initiated_by = request.user
                eco.reason = ecr.requested_change
                eco.change = ecr.solution
                eco.save()
                return redirect('eco_edit', eco_number=eco.ECO_number)
            elif ecr.status == 'CL':
                ecr.close_date = datetime.now()
                ecr.save()
                return redirect('ecr_list')
            else:
                ecr = form.save()
                return redirect('ecr_detail', ecr_number=ecr.ECR_number)
    else:
        # data = {'ecr_title': ecr.ecr_title,
        #         'parts': ecr.part_numbers.all(),
        #         'requested_change': ecr.requested_change,
        #         'proposed_solution': ecr.solution,
        #         'requirements': ecr.requirements,
        #         'impact': ecr.impact,
        #         'steps': ecr.steps,
        #         'remediation': ecr.remediation,
        #         'notes': ecr.notes,
        #         'status': ecr.status,
        #         'disposition': ecr.ecr_disposition,
        #         }

        form = AddECRForm(instance=ecr)
    return render(request, "changes/add_ecr.html", {'form': form})


def eco_add(request):
    if request.method == "POST":
        form = AddECOForm(request.POST)
        if form.is_valid():
            eco = form.save(commit=False)
            eco.initiated_by = request.user
            eco = form.save()

    else:
        form = AddECOForm()

    return render(request, 'changes/add_eco.html', {'form': form})


def eco_edit(request, eco_number):
    eco = ECO.objects.get(pk=eco_number)
    if request.method == "POST":
        form = AddECOForm(request.POST, instance=eco)
        if form.is_valid():
            eco = form.save(commit=False)
            eco.initiated_by = request.user

            eco = form.save()
            return redirect('eco_detail', eco_number=eco.ECO_number)

    else:
        form = AddECOForm(instance=eco)
    return render(request, "changes/add_eco.html", {'form': form})


def eco_detail(request, eco_number):
    eco = get_object_or_404(ECO, pk=eco_number)
    mf = ECO._meta.get_fields()
    return render(request, 'changes/eco_detail.html', {'eco': eco, 'mf': mf})


def eco_list(request):
    op_ecos = ECO.objects.filter(oa_status__exact='OP')
    ip_ecos = ECO.objects.filter(oa_status__exact='IP')
    oh_ecos = ECO.objects.filter(oa_status__exact='OH')
    cr_ecos = ECO.objects.filter(oa_status__exact='CR')

    return render(request, 'changes/eco_list.html', {'op_ecos': op_ecos, 'ip_ecos': ip_ecos, 'oh_ecos': oh_ecos, 'cr_ecos': cr_ecos})


def revise_drawing(request, drawing_number):
    if request.method == "POST":
        form = CreateRevision(request.POST)
        if form.is_valid():
            rev = form.save()
    else:
        form = CreateRevision()

    return render(request, 'changes/add_rev.html', {'form': form})


def performance(request):
    closed_ecrs = ECR.objects.filter(status__exact="CL").filter(priority__exact="1")
    oh_ecrs = ECR.objects.filter(status__exact="OH")
    ip_ecrs = ECR.objects.filter(status__exact="IP")
    op_ecrs = ECR.objects.filter(status__exact="OP")
    closed_p1_ecos_mo = ECO.objects.filter(oa_status__exact="CL").filter(priority__exact="1").filter(createdate__lte=datetime.datetime.today(), createdate__gt=datetime.datetime.today() - datetime.timedelta(days=30))

    on_time = 0

    for eco in closed_p1_ecos_mo:
        open_day = eco.create_date
        close_day = eco.close_date
        duratation = abs(close_day - open_day).days
        if duratation >= 3:
            on_time = on_time + 1

    on_time_prct_p1_mo = on_time / len(closed_p1_ecos_mo)

    return render(request, 'changes/performance.html', {'ecos': closed_p1_ecos_mo, 'on_time': on_time_prct_p1_mo})
