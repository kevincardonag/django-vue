from django.urls import path

from reports.views import ReportView, ReportCreateView

app_name = 'reports'
urlpatterns = [
    path('create/<int:type>/', ReportCreateView.as_view(), name='create'),
    path('index/', ReportView.as_view(), name='index'),
]

