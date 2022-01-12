from django.db.models import fields
from rest_framework import serializers
from .models import *



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = 'text'.split()
        fields = '__all__'     


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'is_active'.split()



class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
    
    def get_tags(self, product):
        return TagSerializer(product.tags.filter(is_active=True), many=True).data
   



class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ["title", "descriptions", "price"]