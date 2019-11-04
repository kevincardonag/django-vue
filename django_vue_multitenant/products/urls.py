from django.urls import path

from plans.views import PlanListView, PlanCreateView, PlanDetailView, PlanDeleteView, PlanUpdateView
from products.views import IngredientCreateView, IngredientDeleteView, IngredientUpdateView, IngredientDetailView, \
    IngredientListView

app_name = 'Ingredients'
urlpatterns = [
    path('', IngredientListView.as_view(), name='list_ingredients'),
    path('create', IngredientCreateView.as_view(), name='create_ingredients'),
    path('delete/<int:pk>/', IngredientDeleteView.as_view(), name='delete_ingredients'),
    path('update/<int:pk>/', IngredientUpdateView.as_view(), name='update_ingredients'),
    path('detail/<int:pk>/', IngredientDetailView.as_view(), name='detail_ingredients'),
]