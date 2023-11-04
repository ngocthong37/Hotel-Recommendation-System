from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('home', views.get_home, name='home'),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('test', views.recommend_hotel_by_city_feature),
    path('booking_detail/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('hotel/<int:hotelcode>', views.hotel_detail, name='hotel_detail'),
    path('rate_hotel/', views.rate_hotel, name='rate_hotel'),
    path('rating_list/', views.rating_list, name='rating_list'),
    path('add_wishlist/<int:roomid>', views.add_wishlist, name='add_wishlist'),
    path('new_booking/<int:roomid>', views.new_booking, name='new_booking'),
]   
