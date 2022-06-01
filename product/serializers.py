from rest_framework import serializers

from cart import favorites
from .models import Product, CollectionProducts, Slider
from about_us.models import Benefits


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id get_images title text size_range collection price discount new_price'.split()



class ProductListSerializer(serializers.ModelSerializer):
    favo = serializers.SerializerMethodField('fav')

    class Meta:
        model = Product
        fields = 'id get_images title text size_range collection price discount new_price favo'.split()

    def fav(self, obj):
        favorites = self.context.get('fav')
        print(favorites)
        if obj.id in favorites:
            return {'fav': True}
        return {'fav': False}


class ProductCartSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField('get_context')

    class Meta:
        model = Product
        fields = 'id get_images title text size_range collection price discount new_price quantity'.split()

    def get_context(self, obj):
        quantity = self.context.get('quantity')[str(obj.id)]['quantity']
        return quantity


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


class CallbackSesializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=5)
    phone = serializers.CharField(max_length=100)