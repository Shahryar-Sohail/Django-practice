from django import forms
from .models import ProjectDetail

class ProjectDetailForm(forms.Form):
    project_Details = forms.ModelChoiceField(queryset=ProjectDetail.objects.all(), label="Select Project Details")