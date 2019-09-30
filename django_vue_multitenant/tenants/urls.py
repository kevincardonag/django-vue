
from django.urls import path
from tenants.views import PizzeriaListView, RequestPizzeriaCreateView, RequestPizzeriaListView

app_name = 'tenants'
urlpatterns = [
      path('', PizzeriaListView.as_view(), name='index'),
      path('create-request/<int:pk>/', RequestPizzeriaCreateView.as_view(), name='create_request'),
      path('request-tenant/', RequestPizzeriaListView.as_view(), name='request_tenant'),
]
