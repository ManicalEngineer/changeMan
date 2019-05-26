from django import forms
from django.forms import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import ECR, ECO, Revision
from parts.models import Part


class AddECRForm(forms.ModelForm):

    class Meta:
        model = ECR
        fields = ('ecr_title', 'part_numbers', 'requested_change',
                  'solution', 'requirements', 'impact', 'steps', 'remediation', 'notes', 'status',
                  'ecr_disposition'
                  )
        widgets = {
            'part_numbers': FilteredSelectMultiple(Part, is_stacked=True),
            'requested_change': widgets.Textarea(),
            'solution': widgets.Textarea(),
            'requirements': widgets.Textarea(),
            'impact': widgets.Textarea(),
            'steps': widgets.Textarea(),
            'remediation': widgets.Textarea(),
            'notes': widgets.Textarea(),
        }

    class Media:
        css = {
            'all': ('/static/css/form.css',),
        }
        # jsi18n is required by the widget
        js = ('/static/javascript/jsi18n.js',)


class AddECOForm(forms.ModelForm):

    class Meta:
        model = ECO
        fields = ('deadline', 'ECR_number', 'part_numbers', 'product', 'engineer', 'change',
                  'reason', 'go', 'go_status', 'go_notes', 'test', 'test_status', 'test_notes',
                  'calcs', 'calcs_status', 'calcs_notes', 'archive', 'archive_status', 'archive_notes',
                  'part', 'part_status', 'part_notes', 'drawings', 'drawings_status', 'drawings_notes',
                  'jigs', 'jigs_status', 'jigs_notes', 'patterns', 'patterns_status', 'patterns_notes',
                  'priority', 'eng_sign', 'oa_status',
                  )
        widgets = {
            'part_numbers': FilteredSelectMultiple(Part, is_stacked=True),
            'deadline': widgets.SelectDateWidget(),
            'change': widgets.Textarea(),
            'reason': widgets.Textarea(),
            'test_notes': widgets.Textarea(),
            'go_notes': widgets.Textarea(),
            'test_notes': widgets.Textarea(),
            'calcs_notes': widgets.Textarea(),
            'archive_notes': widgets.Textarea(),
            'part_notes': widgets.Textarea(),
            'drawings_notes': widgets.Textarea(),
            'jigs_notes': widgets.Textarea(),
            'patterns_notes': widgets.Textarea(),
        }

    class Media:
        css = {
            'all': ('/static/css/form.css',),
        }
        # jsi18n is required by the widget
        js = ('/static/javascript/jsi18n.js',)


class CreateRevision(forms.ModelForm):

    class Meta:
        model = Revision
        fields = ('revised_drawing', 'revision_level', 'description', 'ECO_number')
