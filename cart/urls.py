from django.urls import path
from .views import (CartAddAPIView, CartListAPIView, CartDeleteAPIView, FavoritesAddAPIView, FavoritesListAPIView, FavoritesDeleteAPIView)


urlpatterns = [
    path('api/v1/cart/', CartListAPIView.as_view()),
    path('api/v1/cart/add/<int:id>/', CartAddAPIView.as_view()),
    path('api/v1/cart/remove/<int:id>/', CartDeleteAPIView.as_view()),
    path('api/v1/favorites/', FavoritesListAPIView.as_view()),
    path('api/v1/favorites/add/<int:id>/', FavoritesAddAPIView.as_view()),
    path('api/v1/favorites/delete/<int:id>/', FavoritesDeleteAPIView.as_view()),
    
]
