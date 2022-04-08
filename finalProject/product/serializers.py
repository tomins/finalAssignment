from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "manufacturer",
            "price",
            "stock_level",
            "get_image",
            "get_thumbnail",
        )