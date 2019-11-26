from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from core.views import LandingTemplateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('client.urls', namespace='clients')),
    path('admin/', include('products.urls', namespace='products')),
    path('social-auth/', include('social_django.urls', namespace="social")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
