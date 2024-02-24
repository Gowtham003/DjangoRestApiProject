from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.product_detail_api_view), # localhost:8000/api/products/1/
    path('', views.product_list_create_api_view), # localhost:8000/api/products/
    path('<int:pk>/update/', views.product_update_api_view), # localhost:8000/api/products/1/update/
    path('<int:pk>/delete/', views.product_destroy_api_view), # localhost:8000/api/products/1/delete/
]