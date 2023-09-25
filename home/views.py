from django.shortcuts import render

# from .hotel_recomemdation import ratebased 

# Create your views here.
def get_home(request):
    return render(request, 'home.html') 

# def recommend_hotels(request):
#     # Đoạn logic xử lý yêu cầu của người dùng và gọi hàm ratebased
#     city = request.GET.get('city')
#     number = int(request.GET.get('number'))
#     features = request.GET.get('features')
    
#     recommended_hotels = ratebased(city, number, features)
    
#     # Trả kết quả về template hoặc API response
#     return render(request, 'home.html')