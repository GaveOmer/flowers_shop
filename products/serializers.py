from rest_framework import serializers
from .models import Product, ProductCategory

class ProductListSerializer(serializers.ModelSerializer):
  category = serializers.SlugRelatedField(
    slug_field='name',
    queryset=ProductCategory.objects.all()
  )
  class Meta:
    model = Product
    fields = '__all__'  
    

class ProductDetailSerializer(serializers.ModelSerializer):
  category = serializers.SlugRelatedField(
    slug_field='name',
    queryset=ProductCategory.objects.all()
  )
  
  class Meta:
    model = Product
    fields = '__all__'    
  def __init__(self, *args, **kwargs):
    super(ProductDetailSerializer, self).__init__(*args, **kwargs)
    self.Meta.depth = 1