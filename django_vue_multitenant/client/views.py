from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def landingpage(request):
    return  render(request=request,
                   template_name='client/landing.html')
    # return  HttpResponse('<h2>Hola<h2>')
    # return TemplateView.as_view(template_name="client/landing.html")