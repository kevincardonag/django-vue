
from django.urls import path
from . import views
#from tenants.views import PizzeriaListView

app_name = 'client '

urlpatterns = [
      #path('', PizzeriaListView.as_view(), name='tenant_list'),
      path('', views.landingpage, name='clientlandingpage'),
]