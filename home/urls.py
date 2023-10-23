from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('home', views.recommend_hotels_by_city_base),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
]   
