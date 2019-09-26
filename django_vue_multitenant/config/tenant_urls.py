from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path("", TemplateView.as_view(template_name="application.html"), name="app",),
    # url(r'^', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
