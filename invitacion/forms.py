from django import forms
from invitacion import models

class Invitacion(forms.ModelForm):
    class Meta:
        model = models.Invitacion
        fields = ["invitado"]
        
        widgets = {'invitado': forms.TextInput(attrs = {'class': 'input-guests', 'autocomplete': 'off'}),}
        