from rest_framework import serializers

from products.models import (Ingredient,Category,Product)

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name','price')
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ingredient = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    # ingredient = IngredientSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id','name','code','price','image','description','stock','ingredient','category')

