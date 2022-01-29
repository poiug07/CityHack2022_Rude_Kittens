from django import forms
from predict.models import DataFile

class FileForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ["name", "filepath"]