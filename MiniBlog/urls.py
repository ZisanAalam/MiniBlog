
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.static import serve
from django.conf.urls import url
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('Blog.urls') ),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),  
]
