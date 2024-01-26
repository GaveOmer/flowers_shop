from django.urls import path
from api.spectacular.urls import urlpatterns as doc_urls
app_name='api'

urlpatterns=[]

...
urlpatterns += doc_urls
