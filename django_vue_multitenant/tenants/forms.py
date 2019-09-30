from django import forms
from parsley.decorators import parsleyfy

from tenants.models import PizzeriaRequest


@parsleyfy
class PizzeriaRequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PizzeriaRequestForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'rows': 3, 'cols': 5})

    class Meta:
        model = PizzeriaRequest
        fields = ['name', 'last_name', 'phone', 'email', 'comment']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'phone': 'Teléfono',
            'email': 'Email',
            'comment': 'Comentario',
        }
