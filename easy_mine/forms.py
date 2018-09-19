from django import forms
from .validators import validate_file_extension
from .models import Project, Status, Type, Ticket

class UploadFileForm(forms.Form):
    file = forms.FileField(
         label='Select a file  ',
         validators=[validate_file_extension]
         )
    target = forms.CharField(max_length=200)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_title', 'ticket_details', 'project_id', 'status_id', 'type_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_id'].queryset = Project.objects.none()    
        self.fields['status_id'].queryset = Status.objects.none() 
        self.fields['type_id'].queryset = Type.objects.none() 

           