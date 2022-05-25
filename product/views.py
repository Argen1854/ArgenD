from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import CollectionProducts, Product
from .serializers import CollectionSerializer, ProductListSerializer, ProductDetailSerializer
from rest_framework import status
from rest_framework import pagination


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()    
    serializer_class = ProductListSerializer


class ProductDetailAPIView(APIView):
    def get(self, request, id):
        try:    
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
        data = ProductDetailSerializer(product).data
        return Response(data=data)


class CollectionListAPIView(ListAPIView):
    queryset = CollectionProducts.objects.all()
    pagination_class = pagination.PageNumberPagination
    serializer_class = CollectionSerializer
