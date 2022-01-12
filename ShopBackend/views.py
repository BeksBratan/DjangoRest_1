import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, ProductDetailSerializer, ReviewSerializer
from .models import Product, Review


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found!'})
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)

# @api_view(['GET'])
# def reviews_list_view(request):
#     reviews = Review.objects.all()
#     data = ReviewSerializer(reviews, many=True).data
#     return Response(data=data)



    
