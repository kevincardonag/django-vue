
from django.urls import path
from tenants.views import PizzeriaListView

app_name = 'tenants'
urlpatterns = [
      path('', PizzeriaListView.as_view(), name='tenant_list'),
]
