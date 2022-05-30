from django.urls import path
from .views import ProductListAPIView, CollectionListAPIView, CollectionDetailAPIView, ProductDetailAPIView, MainPageAPIView, SearchAPIView


urlpatterns = [
    path('api/v1/main/', MainPageAPIView.as_view()),
    path('api/v1/main/search/', SearchAPIView.as_view()),
    path('api/v1/products/', ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', ProductDetailAPIView.as_view()),
    path('api/v1/collection/', CollectionListAPIView.as_view()),
    path('api/v1/collection/<int:id>/', CollectionDetailAPIView.as_view()),
]