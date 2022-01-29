from django import forms
from predict.models import DataFile

class FileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder": "File Name",
            "aria-label": "Filename",
            "aria-describedby": "addon-wrapping"
        }
    ))
    filepath = forms.FileField(widget=forms.FileInput(
        attrs={
            "class": "form-control",
        }
    ))

    class Meta:
        model = DataFile
        fields = ["name", "filepath"]