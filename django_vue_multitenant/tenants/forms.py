from django import forms
from parsley.decorators import parsleyfy

from tenants.models import PizzeriaRequest, Pizzeria


@parsleyfy
class PizzeriaRequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PizzeriaRequestForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'rows': 3, 'cols': 5})

    class Meta:
        model = PizzeriaRequest
        fields = ['representative_full_name', 'phone', 'email', 'comment', "company_name", "address"]


@parsleyfy
class PizzeriaForm(forms.ModelForm):

    domain = forms.CharField(label='Dominio', max_length=100)

    def __init__(self, *args, **kwargs):
        super(PizzeriaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pizzeria
        fields = ['name']
        labels = {'name': 'Nombre Schema'}

