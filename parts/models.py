from django.db import models
from django.conf import settings

from changes import models as chModel

# Create your models here.


class Part(models.Model):
    part_number = models.CharField(max_length=30, primary_key=True)
    part_description = models.CharField(max_length=30)
    has_drawing = models.BooleanField()
    create_date = models.DateField(auto_now_add=True)
    initiated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #revision = models.ForeignKey('changes.Revision', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        rtn_str = self.part_number + ' - ' + self.part_description
        return rtn_str

# class Drawing(models.Model):
    #part_number = models.ForeignKey('Part', on_delete=models.CASCADE)
    #dwg_revision = models.ForeignKey('changes.Revision', on_delete=models.CASCADE, blank=True)

    # def __str__(self):
        # return self.part_number + " REV " + self.dwg_revision
