from django.urls import path

from .views import ProductDetailAPIView, ProductListAPIView

app_name = 'api'

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
