from django.urls import path
from .views import ProductDetail, ProductList
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
  #products
  path('products/', ProductList.as_view(), name='product-list'),
  path('product/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)