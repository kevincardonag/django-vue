    
from django.urls import path
from orders.views import OrdertListView,OrderUpdateView,OrderDetailView

app_name = 'products'
urlpatterns = [
    path('', OrdertListView.as_view(), name='index'),
    path('update-order/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('detail/<int:pk>/', OrderDetailView.as_view(), name='detail'),
]
