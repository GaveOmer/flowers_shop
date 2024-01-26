from django.contrib import admin
from django.urls import path, include 
from drf_spectacular.views import SpectacularSwaggerView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('schema/', SpectacularSwaggerView.as_view(), name='schema'),
]
