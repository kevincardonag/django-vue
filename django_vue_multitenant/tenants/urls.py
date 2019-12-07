
from django.urls import path
from tenants.views import PizzeriaListView, RequestPizzeriaCreateView, RequestPizzeriaListView, PizzeriaCreateView, \
      PizzeriaDeleteView, RequestRetirePizzeriaView
from tenants.views import RequestPizzeriaDetailView, RequestPizzeriaDeleteView
app_name = 'tenants'
urlpatterns = [
      path('', PizzeriaListView.as_view(), name='index'),
      path('create-request/<int:pk>/', RequestPizzeriaCreateView.as_view(), name='create_request'),
      path('request-tenant/', RequestPizzeriaListView.as_view(), name='request_tenant'),
      path('delete-request-tenant/<int:pk>/', RequestPizzeriaDeleteView.as_view(), name='delete_request_tenant'),
      path('detail-request-tenant/<int:pk>/', RequestPizzeriaDetailView.as_view(), name='detail_request_tenant'),
      path('create-pizzeria/<int:pk>/', PizzeriaCreateView.as_view(), name='create_pizzeria'),
      path('delete-pizzeria/<int:pk>/', PizzeriaDeleteView.as_view(), name='delete_pizzeria'),
      path('requested-to-retire/<int:pk>/', RequestRetirePizzeriaView.as_view(), name='requested_retire'),
]
