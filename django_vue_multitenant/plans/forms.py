from django.forms import ModelForm
from parsley.decorators import parsleyfy

from plans.models import Plan


@parsleyfy
class PlanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': 3, 'cols': 5})

    class Meta:
        model = Plan
        fields = ['name', 'price', 'description']
        labels = {
            'name': 'Nombre',
            'price': 'Precio',
            'description': 'Descripción',
        }
