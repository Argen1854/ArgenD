from itertools import product
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, CollectionProducts, Slider
from .serializers import ProductListSerializer, CollectionSerializer, ProductDetailSerializer, BenefistSerializer, SliderSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.db.models import Q
from about_us.models import Benefits


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()    
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer


class MainPageAPIView(APIView):
    def get(self, request):
        slider = Slider.objects.all()
        hit = Product.objects.filter(checkbox_hit=True)
        new = Product.objects.filter(checkbox_new=True)
        collection = CollectionProducts.objects.all()
        b = Benefits.objects.all()
        slider_image = SliderSerializer(slider, many=True).data
        hit = ProductListSerializer(hit[:8], many=True).data
        new = ProductListSerializer(new[:4], many=True).data
        collections = CollectionSerializer(collection[:4], many=True).data
        b_s = BenefistSerializer(b, many=True).data
        return Response(data=[{'slider_image': slider_image ,'hit': hit, 'new':new, 'Collection':collections, 'Benefist': b_s}])


class ProductDetailAPIView(APIView):
    def get(self, request, id):
        try:    
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
        products = Product.objects.filter(~Q(id = product.id) & Q(collection_id = product.collection_id))
        data_2 = ProductListSerializer(products[:5], many=True).data
        data = ProductDetailSerializer(product).data
        return Response(data=[data, data_2])


class CollectionListAPIView(ListAPIView):
    queryset = CollectionProducts.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CollectionSerializer


class SearchAPIView(ListAPIView):
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer


    def get_queryset(self):
        search = self.request.GET['search']
        if Product.objects.filter(title__contains=search).count() == 0:
            return {'message': f'По запросу {search} ничего не найдено'}
        return Product.objects.filter(title__contains=search)


class CollectionDetailAPIView(ListAPIView):
    queryset = Product.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ProductListSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        new = Product.objects.filter(checkbox_new = True)[:5]
        new_s = ProductListSerializer(new, many=True).data

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'collection':serializer.data, 'new': new_s})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(collection_id=id)

    