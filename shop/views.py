from itertools import product
import re
from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models


@api_view(['GET'])
def products_list_view(request):
    products = models.Product.objects.all()
    data = serializers.ProductListSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def products_detail_view(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = serializers.ProductDetailSerializer(product, many=True).data
    return Response(data=data)

# @api_view(['PUT', 'DELETE'])
# def products_datail_view(request, id):
#     if request.method == 'PUT':
#         pass
#     elif request.method == "DELETE":
#         product.delete()
#         return Response(data={"Product was delete"})


@api_view(['GET'])
def products_reviews_view(request):
    products = models.Product.objects.all()
    data = serializers.ProductReviewSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def products_tags_view(request):
    products = models.Product.objects.all()
    data = serializers.ProductTagsSerializer(products, many=True).data
    return Response(data=data)











