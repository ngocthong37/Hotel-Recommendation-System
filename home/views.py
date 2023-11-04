from django.shortcuts import render,redirect, get_object_or_404
from .hotel_recomemdation import requirementbased, random_forest_based, citybased
from .models import *
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.func import *
from django.core.exceptions import ObjectDoesNotExist
from .hotel_search import *
# Create your views here.

def search(request):
    if request.method == "POST":
        country = request.POST['country'] 
        description_hotel = request.POST['descriptionHotel'] 
        city = request.POST['city'] 
        rating = request.POST['rating'] 
        number_of = request.POST['numberOf']
        print("in search: ", city, number_of, description_hotel)
        output = citybased(city)
        print('out put search: ',output)
    context = {}
    return render(request,'search.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.name = request.POST['first_name'] + ' ' + request.POST['last_name'] # Lấy giá trị tên từ biểu mẫu
            user_profile.email = request.POST['email']  # Lấy giá trị email từ biểu mẫu
            user_profile.password = request.POST['password1']  # Lấy giá trị mật khẩu từ biểu mẫu
            user_profile.save()
            return redirect('login')
        else: 
            message = "Account already exists, please try again!"
            return render(request, 'register.html', {'message': message} )
    context ={'form':form}
    return render(request,'register.html',context)

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
        else: 
            message = "Wrong username or password. Please try again!"
            return render(request, 'login.html', {'message': message})
    context ={}
    return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect(loginPage)

def get_home(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    username = request.user.first_name + " " + request.user.last_name
    user_profile = UserProfile.objects.get(user=request.user) 
    try:
        userPreferences = UserPreferences.objects.get(user=user_profile)
    except ObjectDoesNotExist:
        userPreferences = None 
    if userPreferences is not None:
        print(userPreferences.number)
        print(userPreferences.city)
        print(userPreferences.feature)
        hotel_list = get_hotels_data_by_codes(random_forest_based(userPreferences.city, userPreferences.number, userPreferences.feature))
        print(hotel_list)
    else:
        city = 'london'
        number = 4
        features = 'I need a room with free wifi'
        hotel_list = get_hotels_data_by_codes(random_forest_based(city, number, features))
        print(hotel_list) # userPreferences không tồn tại, thực hiện xử lý khi không có userPreferences
    
    context = {'username': username, 'result': hotel_list}
    return render(request, 'home.html', context) 

def recommend_hotels_by_requirement(request):
    city = 'london'
    number = 4
    features = 'I need a room with heating'
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
    print('output',output)
    # print(output)
    return render(request, 'home.html')

def new_booking(request):
    if request.method == 'POST':
        hotel_id = request.POST['hotelID']
        user_id = UserProfile.objects.get(user=request.user)
        create_at = datetime.now()
        bookHotel(user_id, hotel_id, create_at)
        return redirect('booking_list')
    else:
        users = User.objects.all()
        return render(request, 'new_booking.html', {'users': users})

def booking_detail(request, booking_id):
    booking = get_object_or_404(BookingHotel, booking_id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

def booking_list(request):
    user = UserProfile.objects.get(user=request.user)
    bookings = BookingHotel.objects.filter(user=user)
    return render(request, 'booking_list.html', {'bookings': bookings})

def add_wishlist(request):
    if request.method == "POST":
        hotel_id = request.POST.get("hotel_id")
        user = UserProfile.objects.get(user=request.user)  # Lấy UserProfile của người dùng đang đăng nhập

        # Lồng đoạn code vào trong view
        wish_list_item, created = WishList.objects.get_or_create(user=user, hotelID=hotel_id)

        return redirect("wishlist")  # Chuyển hướng đến trang wishlist sau khi thêm

    return render(request, "add_wishlist.html")

def wishlist(request):
    user = UserProfile.objects.get(user=request.user) 
    wishlist_items = WishList.objects.filter(user=user)
    return render(request, "wishlist.html", {'wishlist_items': wishlist_items})


def hotel_detail(request,hotelcode):
    listroom = get_room_in_hotel(hotelcode)
    context = {'listroom':listroom}
    return render(request,'hotel_detail.html',context)

def rate_hotel(request):
    if request.method == 'POST':
        hotel_id = request.POST.get('hotel_id')
        value = request.POST.get('value')
        user = UserProfile.objects.get(user=request.user)

        rating = Rating.objects.create(
            user=user,
            hotelID=hotel_id,
            value=value
        )

        return redirect('rating_list')

    return render(request, 'rate_hotel.html')

def rating_list(request):
    ratings = Rating.objects.all()
    return render(request, 'rating_list.html', {'ratings': ratings})

