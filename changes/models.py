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
        ('NA', '------'),
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
    part_numbers = models.ManyToManyField("parts.Part", verbose_name="Affected Part Numbers", blank=True, null=True)

    description = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='IP')
    ecr_disposition = models.CharField(max_length=3, choices=DISPO_CHOICES, null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default='1')
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.ECR_number)


class Notes(models.Model):
    ecr_number = models.ForeignKey('ECR', on_delete=models.CASCADE, verbose_name="Related ECR Number", null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=300, blank=True, null=True)


class Revision(models.Model):
    id = models.AutoField(primary_key=True)
    revised_drawing = models.ForeignKey('parts.Part', on_delete=models.CASCADE, verbose_name="Affected Drawings")
    revision_level = models.CharField(max_length=1, verbose_name="Revision")
    description = models.CharField(max_length=100, verbose_name="Change Description")
    ECR_number = models.ForeignKey('ECR', on_delete=models.CASCADE, verbose_name="Related ECR Number", null=True, blank=True)

    def __str__(self):
        rtn_str = self.revised_drawing.part_number + " Revision " + self.revision_level
        return rtn_str
