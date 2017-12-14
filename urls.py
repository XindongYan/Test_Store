"""MyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from App import views as views

urlpatterns = [
    url(r'^self', views.self),
    url(r'^Car', views.Car),
    url(r'^ShoppingCart', views.ShoppingCart),
    url(r'^(\d+)', views.id, name='id'),
    url(r'^store_post', views.index2),
    url(r'^ages', views.images),
    url(r'^img', views.img),
    url(r'^div', views.div),
    url(r'^new', views.new),
    url(r'^Administrators', views.login),
    url(r'^a', views.Administrators),
    url(r'^store', views.store),
    url(r'register', views.register),
    url(r'^zhuce', views.zhuce),
    url(r'denglu', views.denglu),
    url(r'^login', views.login),
    url(r'^delete', views.delete),
    url(r'^logout', views.logout),
    url(r'^', views.index),
]
