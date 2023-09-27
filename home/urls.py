from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('home', views.recommend_hotel_by_city)
]
