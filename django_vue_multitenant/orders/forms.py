from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from parsley.decorators import parsleyfy
from orders.models import Order,OrderDetail


@parsleyfy
class OrderForm(ModelForm):

    class Meta:
        model = Order   
        fields = ['state']

# @parsleyfy
# class ProductForm(ModelForm):

#     def __init__(self, *args, **kwargs):
#         ingredient = ModelMultipleChoiceField(queryset=Ingredient.objects.all(), widget=CheckboxSelectMultiple(),
#                                               label="Ingredientes")
#         super(ProductForm, self).__init__(*args, **kwargs)
#         self.fields['description'].widget.attrs.update({'rows': 3, 'cols': 5})
#         self.fields['ingredient'] = ingredient

#     class Meta:
#         model = Product
#         fields = ['name', 'code', 'price', 'stock', 'description', 'image', 'ingredient']
#         labels = {
#             'name': 'Nombre',
#             'code': 'Código',
#             'price': 'Precio',
#             'stock': 'Cantidad en stock',
#             'description': 'Descripción',
#             'ingredient': 'Ingredientes',
#             'image': 'Imagen',
#         }

