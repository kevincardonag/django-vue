from django.urls import path
from products.views import IngredientCreateView, IngredientDeleteView, IngredientUpdateView, IngredientDetailView, \
    IngredientListView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = 'products'
urlpatterns = [
    path('ingrediets', IngredientListView.as_view(), name='list_ingredients'),
    path('create-ingredient', IngredientCreateView.as_view(), name='create_ingredients'),
    path('delete/<int:pk>/', IngredientDeleteView.as_view(), name='delete_ingredients'),
    path('update/<int:pk>/', IngredientUpdateView.as_view(), name='update_ingredients'),
    path('detail/<int:pk>/', IngredientDetailView.as_view(), name='detail_ingredients'),
    path('', ProductListView.as_view(), name='index'),
    path('create-product', ProductCreateView.as_view(), name='create_product'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('update-product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('detail-product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
]
