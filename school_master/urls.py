from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),#127.0.0.1:8000/home
    path('',include('home.urls')),#127.0.0.1:8000
    path('ckeditor',include('ckeditor_uploader.urls')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)