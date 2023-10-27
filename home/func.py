from datetime import datetime
from .models import BookingHotel, User

def bookHotel(user_id, hotel_id, create_at):
    user = User.objects.get(pk=user_id)
    booking = BookingHotel(user=user, hotelID=hotel_id, date_booking=create_at)
    booking.save()