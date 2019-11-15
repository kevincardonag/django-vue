from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
# router.register(r'ingredients', views.ingredient_list)
router.register(r'orders', views.OrderViewSet)
router.register(r'ordersdetail', views.OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ingredients/<slug>/',views.ingredient_list,name='ingredients'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]