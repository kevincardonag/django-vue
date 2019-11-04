from django.forms import ModelForm
from parsley.decorators import parsleyfy

from products.models import Ingredient


@parsleyfy
class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name', 'price']
