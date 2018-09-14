from django import forms
from .validators import validate_file_extension

class UploadFileForm(forms.Form):
    file = forms.FileField(
         label='Select a file  ',
         validators=[validate_file_extension]
         )
    target = forms.CharField(max_length=200)