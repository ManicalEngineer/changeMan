from django import forms
from django.forms import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import ECR, Notes, Revision, Attachment
from parts.models import Part


class AddECRForm(forms.ModelForm):

    class Meta:
        model = ECR
        fields = ('ecr_title', 'part_numbers', 'description',
                  'description', 'status',
                  'ecr_disposition', 'engineer'
                  )
        widgets = {
            'part_numbers': FilteredSelectMultiple(Part, is_stacked=True),
            'description': widgets.Textarea(),
            'notes': widgets.Textarea(),
        }

    class Media:
        css = {
            'all': ('/static/css/form.css',),
        }
        # jsi18n is required by the widget
        js = ('/static/javascript/jsi18n.js',)


class AddNoteForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('content',)
        widgets = {
            'content': widgets.Textarea(),
        }


class CreateRevision(forms.ModelForm):

    class Meta:
        model = Revision
        fields = ('revised_drawing', 'revision_level', 'description', 'ECR_number')


class UploadForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ('title', 'file', 'ECR_number')
        widgets = {
            'file': widgets.ClearableFileInput(attrs={'multiple': True})
        }
