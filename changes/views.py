from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from datetime import timedelta

from .models import ECR, Revision, Notes
from parts.models import Part
from projects.models import Project
from .forms import AddECRForm, CreateRevision, AddNoteForm, UploadForm

# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        ecrs = ECR.objects.filter(engineer__exact=request.user)
        projects = Project.objects.filter(engineer__exact=request.user)
        return render(request, 'changes/dashboard.html', {'ecrs': ecrs, 'projects': projects})
    else:
        return render(request, 'redirect.html')


def ecr_list(request):
    op_ecrs = ECR.objects.filter(status__exact='OP')
    ip_ecrs = ECR.objects.filter(status__exact='IP')
    oh_ecrs = ECR.objects.filter(status__exact='OH')
    return render(request, 'changes/ecr_list.html', {'op_ecrs': op_ecrs, 'ip_ecrs': ip_ecrs, 'oh_ecrs': oh_ecrs})


def ecr_detail(request, ecr_number):
    ecr = get_object_or_404(ECR, pk=ecr_number)
    notes = Notes.objects.filter(ecr_number__exact=ecr_number)
    mf = ECR._meta.get_fields()

    if request.method == "POST":
        if 'status' in request.POST.dict():
            form = AddECRForm(request.POST, instance=ecr)
            if getattr(ecr, 'status') != form['status'].value():
                ECR.objects.filter(pk=ecr_number).update(status=form['status'].value())
            if getattr(ecr, 'engineer') != form['engineer'].value():
                ECR.objects.filter(pk=ecr_number).update(engineer=form['engineer'].value())
            return redirect('ecr_detail', ecr_number=ecr.ECR_number)
        else:
            form = AddNoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.author = request.user
                note.ecr_number = get_object_or_404(ECR, pk=ecr_number)
                note = form.save()
                return redirect('ecr_detail', ecr_number=ecr.ECR_number)
    else:
        form = AddNoteForm()
        ECRForm = AddECRForm(instance=ecr)

    return render(request, 'changes/ecr_detail.html', {'ecr': ecr, 'mf': mf, 'notes': notes, 'form': form, 'ECRForm': ECRForm})


def ecr_add(request):
    if request.method == "POST":
        form = AddECRForm(request.POST)
        if form.is_valid():
            ecr = form.save(commit=False)
            ecr.initiated_by = request.user

            ecr = form.save()

            #send_mail('Test', 'ECR Created', settings.EMAIL_HOST_USER, ['unhfireboy@yahoo.com'], fail_silently=False)

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
        form = AddECRForm(instance=ecr)
    return render(request, "changes/add_ecr.html", {'form': form})


def revise_drawing(request, drawing_number, ecr_number):
    if request.method == "POST":
        form = CreateRevision(request.POST)
        if form.is_valid():
            rev = form.save()
        return redirect('part_summary', part_number=drawing_number)
    else:

        revs = Revision.objects.filter(revised_drawing__exact=drawing_number).order_by('-revision_level')
        if len(revs) > 0:
            last_rev = revs[0]
            new_rev = chr(ord(last_rev.revision_level) + 1)
        else:
            new_rev = "A"

        form = CreateRevision(initial={'revised_drawing': drawing_number,
                                       'revision_level': new_rev,
                                       'ECRnumber': ecr_number})

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


def file_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Success!</h1>')
    else:
        form = UploadForm()

    return render(request, 'changes/upload.html', {'form': form})
