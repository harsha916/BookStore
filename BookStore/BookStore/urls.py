"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from atexit import register
from multiprocessing.sharedctypes import Value
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import  settings
from BookStoreApp.views import loginpage,mainpage, registerpage,a,b,c,search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginpage,name="loginpage"),
    path('registerpage/',registerpage,name="registerpage"),
    path('mainpage/',mainpage,name="mainpage"),
    path('a/',a,name="a"),
    path('b/',b,name="b"),
    path('c/',c,name="c"),
    path('search/',search,name="search")
]


urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
