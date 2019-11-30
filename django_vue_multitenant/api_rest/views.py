from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import (ProductSerializer,IngredientSerializer,OrderSerializer,OrderDetailSerializer)
from products.models import (Product,Ingredient)
from client.models import (Order,OrderDetail)

import pdb


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

# class OrderViewSet(viewsets.ModelViewSet):
@permission_classes((AllowAny,))
class OrderViewSet(APIView):
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer

    def get(self, format=None):
        order=Order.objects.all()
        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data)

    # {
    #     "client_name": "sadsadaa",
    #     "direction": "sdsad",
    #     "payment_method": "contra_entrega",
    #     "products":[
    #         {
    #             "quantity": 1,
    #             "product": 6
    #         }
    #     ]
    # }
    
    def post(self, request, format=None):
        completedData=self.completeData(request.data)
        serializer = OrderSerializer(data=completedData)

        if serializer.is_valid():
            # pdb.set_trace()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def completeData(self,data):
        
        if data.get('products') == None:

            return False

        data['price_products']=0;     

        for index,product in enumerate(data['products']):

            price=Product.objects.get(pk=product['product']).price
            data['products'][index]['price']=price
            data['price_products']+=(price*data['products'][index]['quantity'])
        
        data['delivery_cost']=3000
        data['total']=data['price_products']+data['delivery_cost']

        data['state']='pedido'

        return data


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer