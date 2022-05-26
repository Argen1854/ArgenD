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


class SearchAPIView(APIView):
    def get(self, request):
        search = request.GET['search']
        products = Product.objects.filter(title__contains=search)
        # if len(products) == 0:
        #     collection = CollectionProducts.objects.all()[:5]
        #     products = []
        #     for i in collection:
                
        #         products.extend(Product.objects.filter(collection_id = i.id)[:1])
        #     return Response(data=[{'products':products}])
        data = ProductListSerializer(products[:12], many=True).data
        return Response(data=data)



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
        return Response(data=[data]+data_2)


class CollectionListAPIView(ListAPIView):
    queryset = CollectionProducts.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CollectionSerializer