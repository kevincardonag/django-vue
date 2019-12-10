from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from core.views import LandingTemplateView, CustomLoginUserView

urlpatterns = [
    path('login/', CustomLoginUserView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('client.urls', namespace='clients')),
    path('admin/', include('products.urls', namespace='products')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    # path('client/', include('client.urls', namespace='clients2')),
    path('products', include('products.urls', namespace='products')),
    path('orders', include('orders.urls', namespace='orders')),
    path('plans/', include('plans.urls', namespace='plans')),
    path('admin/', include('tenants.urls', namespace='tenants')),
    path('apiREST/', include('api_rest.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
