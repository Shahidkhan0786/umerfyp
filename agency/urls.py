"""flydigital URL Configuration

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
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('support/', views.Support),
    path('postproduction/', views.post_production),
    path('porno/', views.Postpro),
    path('custom/', views.Custom),
    path('about/', views.about),
    path('pricingx/', views.pricingx),
    path('order-requirment/', views.order_requirments),
    # path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/")),
    # path('profile/<int:pk>', views.MyProfileDetailView.as_view()),
    path('payment/' , views.payment),
    path('profile/<int:pk>/' , views.ProfileDetailView.as_view()),
    path('profile/edit/<int:pk>/', views.ProfileUpdateView.as_view(success_url="/")),
    path('ordershis/' , views.orders_history),
    path('cancel/<int:id>/' , views.cancelord),
    path('orderd/' , views.orderss_detail),
]
