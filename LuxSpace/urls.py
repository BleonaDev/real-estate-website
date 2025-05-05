# LuxSpace/urls.py
from django.urls import path
from LuxSpace import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from RealEstate import settings

urlpatterns = [

    path('', views.home, name='home'),
    path('deals/', views.deals, name='deals'),
    path('properties/', views.properties, name='properties'),
    path('contact/' , views.contact, name='contact'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path('admin/', admin.site.urls),

]

