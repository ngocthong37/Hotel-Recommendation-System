from django.shortcuts import render

from .hotel_recomemdation import requirementbased 

from .hotel_recomemdation import citybased 

# Create your views here.
def get_home(request):
    return render(request, 'home.html') 

def recommend_hotels_by_requirement(request):
    # Đoạn logic xử lý yêu cầu của người dùng và gọi hàm ratebased
    city = 'london'
    number = 4
    features = 'I need a room with free wifi'
    
    output = requirementbased(city, number, features)
    print(output)
    # Trả kết quả về template hoặc API response
    return render(request, 'home.html')

def recommend_hotel_by_city(request):
    city = "london"
    output = citybased(city)
    print(output)
    return render(request, 'home.html')
