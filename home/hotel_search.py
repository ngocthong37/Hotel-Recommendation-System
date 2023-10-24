import pandas as pd
import csv
import os
import json


current_directory = os.getcwd()

hotel_info_path = os.path.join(current_directory, 'data-set', 'Hotel.csv')
hotel_price_average_path = os.path.join(current_directory, 'data-set', 'HotelPriceSummary.csv')

if os.path.exists(hotel_info_path):
    hotel_info = pd.read_csv(hotel_info_path, delimiter=',')
else:
    print("Tệp tin 'Hotel.csv' không tồn tại.")
if os.path.exists(hotel_price_average_path):
    hotel_price_average = pd.read_csv(hotel_price_average_path, delimiter=',')
else:
    print("Tệp tin 'HotelPriceSummary.csv' không tồn tại.")


def get_hotels_data_by_codes(hotel_codes):
    # Lọc các hàng có hotelcode trong danh sách hotel_codes
    filtered_rows = hotel_price_average[hotel_price_average['hotelcode'].isin(hotel_codes)]
    return filtered_rows

def get_room_in_hotel(hotel_code):
    filtered_rows = hotel_info[hotel_info['hotelcode']==hotel_code]
    return filtered_rows


print(get_room_in_hotel(59961))