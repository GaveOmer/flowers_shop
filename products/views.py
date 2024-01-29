from rest_framework import generics
from . import serializers
from . import models

#product
class ProductList(generics.ListCreateAPIView):
  queryset = models.Product.objects.all()
  serializer_class = serializers.ProductListSerializer
  

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Product.objects.all()
  serializer_class = serializers.ProductDetailSerializer 
  lookup_field = 'slug'

#FILTERS