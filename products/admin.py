from django.contrib import admin

from .models import ProductCategory, Product

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
  list_display = ('id','name','slug')
  list_editable = ('name','slug')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('id','name','slug','category','available','detail','price','stock')
  list_editable=('name','slug','category','available','detail','price','stock')
  

