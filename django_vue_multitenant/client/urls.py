
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from tenants.views import PizzeriaListView

app_name = 'client '

urlpatterns = [
      #path('', PizzeriaListView.as_view(), name='tenant_list'),
      path('', views.landingpage, name='clientlandingpage'),
      path('pizzas/', views.productpage, name='clientpizzas'),
      path('pagar/', views.pagarpage, name='clientpizzas'),
]
