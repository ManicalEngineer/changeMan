from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Requirement)
admin.site.register(Specification)
admin.site.register(Concept)
admin.site.register(Rating)
admin.site.register(Idea)
admin.site.register(Feedback)
