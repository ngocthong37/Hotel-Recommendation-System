import os
import csv
import pandas as pd

current_directory = os.getcwd()
hotel_details_path = os.path.join(current_directory, 'data-set', 'Hotel_details.csv')

if os.path.exists(hotel_details_path):
    hotel_details = pd.read_csv(hotel_details_path, delimiter=',')
else:
    print("Tệp tin 'Hotel_details.csv' không tồn tại.")


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


# Ghép ba cột 'address', 'city', và 'country' thành một cột 'address' trong DataFrame 'hotel_details'
hotel_details['address'] = hotel_details['address'] + ', ' + hotel_details['city'] + ', ' + hotel_details['country']

# Lấy hai cột 'starrating' và 'address' từ DataFrame 'hotel_details'
selected_columns = hotel_details[['hotelid', 'starrating', 'address']]

# Kết hợp 'selected_columns' và 'hotel_info' bằng cột 'hotelcode'
merged_data = pd.merge( hotel_price_average, selected_columns,left_on='hotelcode', right_on='hotelid', how='inner')
# Xóa cột 'hotelid' từ DataFrame
merged_data = merged_data.drop('hotelid', axis=1)

merged_data.to_csv('merged_data.csv', index=False)
