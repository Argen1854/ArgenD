from django.urls import path
from .views import AboutUsAPIView, NewsListAPIView, HelpAPIViews, OfferAPIView


urlpatterns = [
    path('api/v1/about/', AboutUsAPIView.as_view()),
    path('api/v1/news/', NewsListAPIView.as_view()),
    path('api/v1/help/', HelpAPIViews.as_view()),
    path('api/v1/offer/', OfferAPIView.as_view()),
]
