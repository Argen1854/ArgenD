from rest_framework import serializers


class CartSesializer(serializers.Serializer):
    id = serializers.IntegerField()
    image_id = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    second_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=30)
    Country = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
