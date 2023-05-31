from django import forms
from .models import DocJsonFile


class UploadedForm(forms.ModelForm):
    class Meta:
        model = DocJsonFile
        fields = [
            'json_file',
        ]
