from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (ProductSerializer,IngredientSerializer)
from products.models import (Product,Ingredient)



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    def get_queryset(self):
        favorites = self.request.query_params.get('favorites')
        if favorites:
            queryset = Product.objects.all().order_by('name')[:3]
        else:
            queryset = Product.objects.all().order_by('name')
        return queryset
            

# class IngredientViewSet(viewsets.ModelViewSet):
#     queryset = Ingredient.objects.all().order_by('name')
#     serializer_class = IngredientSerializer

# @api_view(['GET'])
# def product_list(request,slug):
#     if request.method == 'GET':
#         product = Product.objects.all().order_by('name')
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data)


@api_view(['GET', 'POST'])
def ingredient_list(request,slug):
    if request.method == 'GET':
        ingredient = Ingredient.objects.all().order_by('name')
        serializer = IngredientSerializer(ingredient, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

