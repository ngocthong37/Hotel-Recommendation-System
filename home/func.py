from datetime import datetime
from .models import *

def bookHotel(user, hotel_id, create_at):
    booking = BookingHotel(user=user, hotelID=hotel_id, date_booking=create_at)
    booking.save()