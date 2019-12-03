from django.contrib import admin
from .models import Notes, ECR, Revision, Attachment

# Register your models here.
admin.site.register(Notes)
admin.site.register(ECR)
admin.site.register(Revision)
admin.site.register(Attachment)
