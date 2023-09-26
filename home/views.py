from django.shortcuts import render

from .hotel_recomemdation import citybased 
from .hotel_recomemdation import requirementbased 
from .hotel_recomemdation import ratebased 



def recommend_hotels_by_requirement(request):
    city = 'london'
    number = 4
    features = 'I need a room with free wifi'
    output = citybased(city)
    return ""

def recommend_hotel_by_city(request):
    city = "city"
    output = citybased(city)
    return ""

def recommend_hotel_by_rating(request):
    city = 'london'
    number = 4
    features = 'I need a room with free wifi'
    output = citybased(city)
    return ""