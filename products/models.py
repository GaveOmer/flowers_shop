from django.db import models


class ProductCategory(models.Model):
  name = models.CharField('Название',max_length=255)
  slug = models.SlugField('URL',max_length=200, unique=True)
  created_at = models.DateTimeField('Время создания',auto_now_add=True)
  updated_at = models.DateTimeField('Время обновления',auto_now=True)
  
  class Meta:
    ordering = ('name',)
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
  
  def __str__(self):
    return self.name
  
class Product(models.Model):
  category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, related_name='products')  
  name = models.CharField('Название продукта',max_length=255,blank=False,null=True)
  slug = models.SlugField('URL', max_length=255, unique=True)
  available = models.BooleanField('Доступно',default=True)
  created_at = models.DateTimeField('Время создания',auto_now_add=True)
  updated_at = models.DateTimeField('Время обновления',auto_now=True)
  detail = models.TextField('Описание',max_length=255, blank=True,null=True)
  price = models.DecimalField('Цена',max_digits=10, decimal_places=2, default=0)
  stock = models.PositiveIntegerField('Количество в наличии',default=0)
  image = models.ImageField('',upload_to='product_images/',blank=True,null=True)
  class Meta:
    ordering = ('name',) 
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'

  def __str__(self):
    return self.name  