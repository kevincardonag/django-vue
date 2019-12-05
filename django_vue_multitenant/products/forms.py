from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from parsley.decorators import parsleyfy
from products.models import Ingredient, Product


@parsleyfy
class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name', 'price']

@parsleyfy
class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        ingredient = ModelMultipleChoiceField(queryset=Ingredient.objects.all(), widget=CheckboxSelectMultiple(),
                                              label="Ingredientes")
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': 3, 'cols': 5})
        self.fields['ingredient'] = ingredient

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'ingredient']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'ingredient': 'Ingredientes',
            'image': 'Imagen',
        }

