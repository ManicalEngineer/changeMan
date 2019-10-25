from django import forms
from django.forms import widgets

from .models import Part


class AddPartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ('part_number', 'part_description', 'drawing_only', 'in_syteline', 'notes')
        widgets = {
            'notes': widgets.Textarea(),
        }
