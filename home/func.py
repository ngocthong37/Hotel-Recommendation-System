from datetime import datetime
from .models import *
from django.http import HttpResponse,JsonResponse

def bookHotel(user, hotel_id, create_at):
    booking = BookingHotel(user=user, hotelID=hotel_id, date_booking=create_at)
    booking.save()

def rateHotel(user, hotel_id, value):
    rating = Rating.objects.create(
            user=user,
            hotelID=hotel_id,
            value=value
        )

def addWishList(user, hotel_id):
    wish_list_item, created = WishList.objects.get_or_create(user=user, hotelID=hotel_id)

def create_user_preference(user_profile, city, number, feature):
    user_preference = UserPreferences.objects.create(
        user=user_profile,
        city=city,
        number=number,
        feature=feature
    )
    return user_preference