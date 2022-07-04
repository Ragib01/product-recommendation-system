from rest_framework import serializers
from .models import *


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class WeatherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherType
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    product_type = ProductTypeSerializer()
    weather_type = WeatherTypeSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = []


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
