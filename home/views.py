from django.shortcuts import render,redirect, get_object_or_404
from .hotel_recomemdation import requirementbased, random_forest_based, citybased
from .models import *
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .func import *
from django.core.exceptions import ObjectDoesNotExist
from .hotel_search import *
# Create your views here.

def search(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    user_profile = UserProfile.objects.get(user=request.user) 
    if request.method == "POST":
        description_hotel = request.POST['descriptionHotel'] 
        city = request.POST['city'] 
        number_of = int(request.POST['numberOf'])
        print("in search: ", city, number_of, description_hotel)
        if number_of is None and description_hotel is None:
            output = citybased(city)
        else:
            output = requirementbased(city,number_of,description_hotel)
            create_user_preference(user_profile,city,number_of,description_hotel,25)
        hotelList = get_hotels_data_by_codes(output)
        print(hotelList)
        context = {'hotelList': hotelList}
        return render(request, 'search.html', context)
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
        userPreferenceslist = UserPreferences.objects.filter(user=user_profile)
    except ObjectDoesNotExist:
        userPreferenceslist = None 
    if userPreferenceslist is not None:
        hotel_code_list =[]
        for userPreferences in userPreferenceslist:
            hotel_code_list = random_forest_based(userPreferences.city, int(userPreferences.number), userPreferences.feature) + hotel_code_list
        print(hotel_code_list)
    else:
        city = 'london'
        number = 4
        features = 'I need a room with free wifi'
        hotel_code_list = random_forest_based(city, number, features)
        print(hotel_code_list) 
    hotel_list = get_hotels_data_by_codes(hotel_code_list)
    context = {'username': username, 'result': hotel_list}
    return render(request, 'home.html', context) 

# def recommend_hotels_by_requirement(request):
#     city = 'london'
#     number = 4
#     features = 'I need a room with heating'
#     output = requirementbased(city, number, features)
#     print(output)
#     return render(request, 'home.html')

# def recommend_hotel_by_city(request):
#     city = "london"
#     output = citybased(city)
#     print(output)
#     return render(request, 'home.html')

# def recommend_hotel_by_city_feature(request):

#     city = "london"
#     number = 4
#     features = 'I need a room with free wifi'
#     output = random_forest_based(city, number, features)
#     print('output',output)
#     # print(output)
#     return render(request, 'home.html')

def new_booking(request, roomid):
    if not request.user.is_authenticated:
        return redirect('login') 
    hotel_id = roomid
    userProfile = UserProfile.objects.get(user=request.user)
    create_at = datetime.now()
    day_in = datetime.strptime('04/11/2023', "%d/%m/%Y")
    day_out = datetime.strptime('08/11/2023', "%d/%m/%Y")
    bookHotel(userProfile, hotel_id, create_at,day_in,day_out)
    user = UserProfile.objects.get(user=request.user)
    bookings = BookingHotel.objects.filter(user=user)
    userPreferences = getUserPreferencesByRoom(roomid)
    create_user_preference(userProfile,userPreferences[0],userPreferences[1],userPreferences[2],50)
    return render(request, 'booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    if not request.user.is_authenticated:
        return redirect('login') 
    booking = get_object_or_404(BookingHotel, booking_id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

def booking_list(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    user = UserProfile.objects.get(user=request.user)
    bookings = BookingHotel.objects.filter(user=user)
    return render(request, 'booking_list.html', {'bookings': bookings})

def add_wishlist(request, roomid):
    if not request.user.is_authenticated:
        return redirect('login') 
    user = UserProfile.objects.get(user=request.user)
    WishList.objects.get_or_create(user=user, roomId=roomid)
    hotelcode = get_hotelcode_by_room(roomid)
    userProfile = UserProfile.objects.get(user=request.user)
    userPreferences = getUserPreferencesByRoom(roomid)
    create_user_preference(userProfile,userPreferences[0],userPreferences[1],userPreferences[2],75)
    return redirect('hotel_detail', hotelcode=hotelcode)


def wishlist(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    user = UserProfile.objects.get(user=request.user) 
    wishlist_items = WishList.objects.filter(user=user)
    return render(request, "wishlist.html", {'wishlist_items': wishlist_items})


def hotel_detail(request,hotelcode):
    if not request.user.is_authenticated:
        return redirect('login') 
    listroom = get_room_in_hotel(hotelcode)
    user = UserProfile.objects.get(user=request.user)
    wishlist_items = set(WishList.objects.filter(user=user).values_list('roomId', flat=True).distinct())
    output = []
    
    for room in listroom:
        room['isWishList'] = str(room['id']) in wishlist_items
        output.append(room)

    context = {'listroom': output}
    return render(request, 'hotel_detail.html', context)

def rate_hotel(request):
    if not request.user.is_authenticated:
        return redirect('login') 
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
    if not request.user.is_authenticated:
        return redirect('login') 
    ratings = Rating.objects.all()
    return render(request, 'rating_list.html', {'ratings': ratings})

