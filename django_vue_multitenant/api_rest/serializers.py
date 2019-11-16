from rest_framework import serializers

from products.models import (Ingredient,Category,Product)
from client.models import (Order,OrderDetail)

import pdb
import copy

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

class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    #product = serializers.SlugRelatedField(many=True, read_only=True, slug_field='id')
    #orderdetail = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    product = serializers.PrimaryKeyRelatedField(
                     queryset=Product.objects.all())
    
    class Meta:
        model = OrderDetail
        fields = ('id','quantity','price','product')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # orderdetail = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.PrimaryKeyRelatedField( many=True,
    #                  queryset=OrderDetail.objects.all())
    products = OrderDetailSerializer(many=True,)
    
    class Meta:
        model = Order
        fields = ('id','client_name','direction','email','payment_method','price_products','delivery_cost','total','date_payment','state','products')

    def create(self, data):
        
        order_detail = data['products']
        order_data = copy.deepcopy(data)
        del order_data['products']
        order = Order.objects.create(**order_data)
        
        for product in order_detail:
            OrderDetail.objects.create(order=order, **product)
        
        return data


