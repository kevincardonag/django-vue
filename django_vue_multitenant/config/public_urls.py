import json

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core.views import LandingTemplateView

urlpatterns = [
      path('', LandingTemplateView.as_view(), name='index'),
      path('admin/', include('tenants.urls', namespace='tenants')),
      path('login/', auth_views.LoginView.as_view(), name='login'),
      path('logout/', auth_views.LogoutView.as_view(), name='logout'),
      path('plans/', include('plans.urls', namespace='plans')),
      path('users/', include('users.urls', namespace='users')),
      path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



