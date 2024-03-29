from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url = 'login')
def landingpage(request):
    username = ""
    name = ""
    direction = ""
    if request.user.is_authenticated:

        username = request.user.email
        name = request.user.get_full_name
        direction = request.user.direction

    return  render(request=request,
                   template_name='client/landing.html', 
                   context={'username': username,'name': name, 'direction': direction})
    # return  render(request, 'client/landing.html',{'title': 'Pizeria'})

def productpage(request):
    username = ""
    name = ""
    direction = ""
    if request.user.is_authenticated:

        username = request.user.email
        name = request.user.get_full_name
        direction = request.user.direction

    return  render(request=request,
                   template_name='client/product.html',
                   context={'username': username,'name': name, 'direction': direction})

def pagarpage(request):
    username = ""
    name = ""
    direction = ""
    if request.user.is_authenticated:
        
        username = request.user.email
        name = request.user.get_full_name
        direction = request.user.direction

    return  render(request=request,
                   template_name='client/pagar.html', 
                   context={'username': username,'name': name, 'direction': direction})