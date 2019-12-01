from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def landingpage(request):
    return  render(request=request,
                   template_name='client/landing.html', context={'title': 'Pizzeria'})
    # return  render(request, 'client/landing.html',{'title': 'Pizeria'})

def productpage(request):
    return  render(request=request,
                   template_name='client/product.html')

def pagarpage(request):
    return  render(request=request,
                   template_name='client/pagar.html')