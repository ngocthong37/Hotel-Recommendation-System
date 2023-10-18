from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class UserPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    feature = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.feature

class BookingHotel(models.Model):
    booking_id = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    hotelName = models.CharField(max_length=200, null=True)
    date_booking = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
        

# class HotelRecommend(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
#     UserPreferences = models.ForeignKey(UserPreferences, on_delete=models.SET_NULL, blank=True, null=True)
#     hotel_recommend = models.CharField(max_length=200, null=True)
#     def __str__(self):
#         return self.hotel_recommend

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    hotelName = models.CharField(max_length=200, null=True)
    saved_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hotel
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotelName = models.CharField(max_length=200, null=True)
    value = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.value