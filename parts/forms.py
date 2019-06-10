from django import forms

from .models import Part


class AddPartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ('part_number', 'part_description')
