from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(UserPreferences)
admin.site.register(BookingHotel)

admin.site.register(WishList)
