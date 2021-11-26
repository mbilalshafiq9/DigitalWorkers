"""DigitalWorkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# IMport Static and Media Files to serve
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

# Customize the text of Super Admin Panel
admin.site.site_header = "Digital Workers Admin"
admin.site.site_title = "Digital Workers Admin Portal"
admin.site.index_title = "Welcome to Digital Workers Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('buyer/', include('Buyer.urls')),
    path('worker/', include('Worker.urls')),

    # GET STATIC and Uploaded Media FIles
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

