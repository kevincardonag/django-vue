from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from django.forms import ModelForm
from django import forms
from parsley.decorators import parsleyfy

from plans.models import Plan


@parsleyfy
class PlanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': 3, 'cols': 5})

    class Meta:
        model = Plan
        fields = ['name', 'price', 'description', "custom_ingredients", "custom_products", "is_basic"]
        labels = {
            'name': 'Nombre',
            'price': 'Precio',
            'description': 'Descripción',
        }


@parsleyfy
class PaymentForm(forms.Form):
    full_name = forms.CharField(label="Nombre")
    identification = forms.IntegerField(label="Idenficación")
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')