from django import forms
from django.forms import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *


class AddRequirement(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = (
            'project',
            'description',
            'justification',
            'shall',
            'weight',
            'approved',
            'approved_date',
        )
        widgets = {
            'project': widgets.Textarea,

        }

    class Media:
        css = {
            'all': ('/static/css/form.css',),
        }
        # jsi18n is required by the widget
        js = ('/static/javascript/jsi18n.js',)


class AddProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = (
            'title',
            'sponsor',
            'engineer',
            'goal',
            'proj_type',
        )
        widgets = {
            'goal': widgets.Textarea(),
        }


class AddSpecificationForm(forms.ModelForm):

    class Meta:
        model = Specification
        fields = (
            'requirements',
            'value_type',
            'goal_value',
            'description',
            'approved',
            'approved_date'
        )
        widgets = {
            'description': widgets.Textarea(),
        }


class AddConceptForm(forms.ModelForm):

    class Meta:
        model = Concept
        fields = (
            'title',
            'description',
            'project',
            'media',
            'selected',
        )
        widgets = {
            'description': widgets.Textarea(),
        }
