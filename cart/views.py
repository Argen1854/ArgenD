from math import prod
from django.shortcuts import get_object_or_404
from .cart import Cart
from rest_framework.views import APIView
from product.models import Product
from rest_framework.response import Response
from product.serializers import ProductSerializer, ProductCartSerializer
from .favorites import Favorites
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


class Page12Pagination(PageNumberPagination):
    page_size = 12

class FavoritesListAPIView(ListAPIView):
    """Список избранного"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Page12Pagination

    def get_queryset(self):
        fav = Favorites(self.request)
        return Product.objects.filter(id__in=fav.show())


class FavoritesAddAPIView(APIView):
    """Добавить товар в избранное"""
    def post(self, request, id):
        fav = Favorites(request)
        product = get_object_or_404(Product, id = id)
        fav.add(product=product)
        return Response(data={'message': 'ok'})


class FavoritesDeleteAPIView(APIView):
    """Удалить из избранного"""
    def post(self, request, id):
        fav = Favorites(request)
        product = get_object_or_404(Product, id = id)
        fav.remove(product=product)
        return Response(data={'message': 'ok'})


class CartListAPIView(APIView):
    """Список корзины"""
    def get(self, request):
        cart = Cart(request)
        product = cart.get_all()
        products = ProductCartSerializer(product, many=True, context={'quantity': cart.cart}).data
        price = cart.get_total_price()
        prices = price['price']
        discount = price['discount_price']
        return Response(data = {'product': products , 'price': prices, 'discount': discount, 'total_price': prices-discount})


class CartAddAPIView(APIView):
    """Добавить товар в корзину"""
    def post(self, request, id):
        card = Cart(request)
        product = get_object_or_404(Product, id = id)
        card.add(product=product)
        return Response(data={'message': 'ok'})


class CartDeleteAPIView(APIView):
    """Удалить товар из корзины"""
    def post(self, request, id):
        card = Cart(request)
        product = get_object_or_404(Product, id = id)
        card.remove(product=product)
        return Response(data={'message': 'ok'})
