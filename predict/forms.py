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
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder": "Some project description...",
            "aria-label": "descriptio",
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
        fields = ["name", "description", "filepath"]

class AccessRequestForm(forms.ModelForm):
    companyName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder": "File Name",
            "aria-label": "Filename",
            "aria-describedby": "addon-wrapping"
        }
    ))

    representativeName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder": "Some project description...",
            "aria-label": "descriptio",
            "aria-describedby": "addon-wrapping"
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class":"form-control",
            "placeholder": "Some project description...",
            "aria-label": "descriptio",
            "aria-describedby": "addon-wrapping"
        }
    ))

    class Meta:
        model = DataFile
        fields = ["name", "representativeName", "email"]