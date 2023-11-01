from django.shortcuts import render,redirect, get_object_or_404
from .hotel_recomemdation import requirementbased, random_forest_based, citybased 
from .models import *
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.func import *
# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(get_home)
    context ={'form':form}
    return render(request,'regiter.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect(get_home)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(get_home)
        else: messages.info(request,'Co gi do chua dung!')
    context ={}
    return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect(loginPage)

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


def recommend_hotel_by_city_feature(request):
    city = "london"
    number = 4
    features = 'I need a room with free wifi'
    output = random_forest_based(city, number, features)
    print(output)
    return render(request, 'home.html')

def new_booking(request):
    if request.method == 'POST':
        user_id = request.POST['user']
        hotel_id = request.POST['hotelID']
        create_at = datetime.now()
        #booking = BookingHotel.objects.create(user_id=user_id, hotelID=hotel_id)
        bookHotel(user_id, hotel_id, create_at)
        return redirect('booking_list')
    else:
        users = User.objects.all()
        return render(request, 'new_booking.html', {'users': users})

def booking_detail(request, booking_id):
    booking = get_object_or_404(BookingHotel, booking_id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

def booking_list(request):
    bookings = BookingHotel.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})