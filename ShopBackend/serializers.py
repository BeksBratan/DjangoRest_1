import re
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
        # fields = 'is_active'.split()
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title descriptions price category tags'.split()
    
    def get_tags(self, product):
        return TagSerializer(product.tags.filter(is_active=True), many=True).data



class ProductDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ["title", "descriptions", "price", "category", "tags"]











