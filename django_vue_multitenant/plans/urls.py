"""superdroguerias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from plans.views import PlanListView, PlanCreateView, PlanDetailView, PlanDeleteView, PlanUpdateView, \
    PlanUpgradeListView, PlanUpgradeUpdateView

app_name = 'plans'
urlpatterns = [
    path('', PlanListView.as_view(), name='index'),
    path('create', PlanCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', PlanDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', PlanUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', PlanDetailView.as_view(), name='detail'),
    path('upgrade-plan', PlanUpgradeListView.as_view(), name='upgrade_plan'),
    path('upgrade-plan-update/<int:pk>/', PlanUpgradeUpdateView.as_view(), name='upgrade_plan_update'),
]