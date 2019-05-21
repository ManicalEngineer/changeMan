from django.db import models
from django.conf import settings

from parts import models as partModels


# Create your models here.


class ECR(models.Model):
    STATUS_CHOICES = (
        ('OH', 'On Hold'),
        ('CL', 'Closed'),
        ('IP', 'In Progress'),
        ('OP', 'Open'),
        )

    DISPO_CHOICES = (
        ('NA','------'),
        ('WNF', 'Will Not Fix'),
        ('FX', 'Fixed'),
        ('ECO', 'Create ECO'),
        ('NT', 'No Trouble Found'),
        )

    PRIORITY_CHOICES = {
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low'),
    }

    create_date = models.DateField(auto_now_add=True)
    ecr_title = models.CharField(max_length=50, blank=True, null=True)
    initiated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    engineer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ECR", blank=True, null=True)
    ECR_number = models.AutoField(primary_key=True, verbose_name="ECR Number")
    part_numbers = models.ManyToManyField("parts.Part", verbose_name="Affected Part Numbers")
    requested_change = models.CharField(max_length=300, verbose_name="Requested Change or Improvement")
    
    solution = models.CharField(max_length=300, verbose_name="Solution & Cost")
    requirements = models.CharField(max_length=300)
    impact = models.CharField(max_length=300)
    steps = models.CharField(max_length=300)
    remediation = models.CharField(max_length=300)
    notes = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='IP')
    ecr_disposition = models.CharField(max_length=3, choices=DISPO_CHOICES, null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default='1')
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.ECR_number)


class ECO(models.Model):
    STATUS_CHOICES = (
        ('OH', 'On Hold'),
        ('CL', 'Closed'),
        ('IP', 'In Progress'),
        ('OP', 'Open'),
        ('CR', 'Created'),
        )

    PRIORITY_CHOICES = {
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low'),
    }

    eco_title = models.CharField(max_length=300, blank=True, null=True)
    create_date = models.DateField(auto_now_add=True, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    ECO_number = models.AutoField(primary_key=True, verbose_name="ECO Number")
    ECR_number = models.ForeignKey('ECR', on_delete=models.CASCADE, verbose_name="Related ECR")
    part_numbers = models.ManyToManyField("parts.Part", verbose_name="Affected Part Numbers")
    product = models.CharField(max_length=50, blank=True, null=True)
    initiated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    engineer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ECO", blank=True, null=True)
    change = models.CharField(max_length=300, blank=True, null=True)
    reason = models.CharField(max_length=300, blank=True, null=True)
    go = models.CharField(max_length=10, blank=True, null=True)
    go_status = models.CharField(max_length=20, blank=True, null=True)
    go_notes = models.CharField(max_length=300, blank=True, null=True)
    test = models.CharField(max_length=10, blank=True, null=True)
    test_status = models.CharField(max_length=20, blank=True, null=True)
    test_notes = models.CharField(max_length=300, blank=True, null=True)
    calcs = models.CharField(max_length=10, blank=True, null=True)
    calcs_status = models.CharField(max_length=20, blank=True, null=True)
    calcs_notes = models.CharField(max_length=300, blank=True, null=True)
    archive = models.CharField(max_length=10, blank=True, null=True)
    archive_status = models.CharField(max_length=20, blank=True, null=True)
    archive_notes = models.CharField(max_length=300, blank=True, null=True)
    part = models.CharField(max_length=10, blank=True, null=True)
    part_status = models.CharField(max_length=20, blank=True, null=True)
    part_notes = models.CharField(max_length=300, blank=True, null=True)
    drawings = models.CharField(max_length=10, blank=True, null=True)
    drawings_status = models.CharField(max_length=20, blank=True, null=True)
    drawings_notes = models.CharField(max_length=300, blank=True, null=True)
    jigs = models.CharField(max_length=10, blank=True, null=True)
    jigs_status = models.CharField(max_length=20, blank=True, null=True)
    jigs_notes = models.CharField(max_length=300, blank=True, null=True)
    patterns = models.CharField(max_length=10, blank=True, null=True)
    patterns_status = models.CharField(max_length=20, blank=True, null=True)
    patterns_notes = models.CharField(max_length=300, blank=True, null=True)
    oa_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Created")
    priority = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default='1')

    def __str__(self):
        return str(self.ECO_number)


class Revision(models.Model):
    id = models.AutoField(primary_key=True)
    revised_drawing = models.ForeignKey('parts.Part', on_delete=models.CASCADE, verbose_name="Affected Drawings")
    revision_level = models.CharField(max_length=1, verbose_name="Revision")
    description = models.CharField(max_length=100, verbose_name="Change Description")
    ECO_number = models.ForeignKey('ECO', on_delete=models.CASCADE, verbose_name="Related ECO Number", null=True, blank=True)

    # def __str__(self):
#    return str(self.revised_drawing) + " Revision " + str(self.revision_level)
