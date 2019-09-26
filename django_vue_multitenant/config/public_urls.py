import json

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import path, include
from django.views import View
from django.views.generic import TemplateView
from core.views import LandingTemplateView


# class test(View):
#     template_name = "application.html"
#
#     def get(self, request, *args, **kwargs):
#         print("hola")
#         rendered = render_to_string('application.html', json.dumps({'foo': 'bar'}))
#         response = HttpResponse(rendered)
#         return response
#
#     def get_context_data(self):
#         context = super(test, self).get_context_data()
#         context['test'] = "hola"
#
#         return context


urlpatterns = [
      path('', LandingTemplateView.as_view(), name='index'),
      path('admin/', include('tenants.urls', namespace='tenants')),
      path('login/', auth_views.LoginView.as_view(), name='login'),
      path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



