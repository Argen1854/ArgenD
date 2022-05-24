from rest_framework import serializers
from .models import Product, CollectionProducts


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id get_images title text price discount size_range'.split()


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id get_images title vendor_code text price discount size_range cloth quantity_in_line material checkbox_hit checkbox_new'.split()

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionProducts
        fields = 'id title image'.split()


