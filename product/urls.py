from django.urls import path
from .views import CollectionListAPIView, ProductDetailAPIView, ProductListAPIView


urlpatterns = [
    path('api/v1/products/', ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', ProductDetailAPIView.as_view()),
    path('api/v1/collection/', CollectionListAPIView.as_view()),
]
