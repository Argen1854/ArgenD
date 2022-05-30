from rest_framework import serializers
from .models import Product, CollectionProducts, Slider
from about_us.models import Benefits

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id get_images title text size_range collection prices'.split()

class MainSerializer(serializers.ModelSerializer):
    def get_attribute(self, instance):
        return super().get_attribute(instance)



class BenefistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = 'images title text'.split()


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id get_images title vendor_code text size_range cloth quantity_in_line material checkbox_hit checkbox_new collection prices'.split()


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionProducts
        fields = 'id title image'.split()


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = 'image link'.split()

