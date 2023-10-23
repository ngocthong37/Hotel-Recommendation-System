from django.shortcuts import render,redirect
from .hotel_recomemdation import citybased, random_forest_based
from .models import *
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
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

def recommend_hotels_by_city_base(request):
    # Đoạn logic xử lý yêu cầu của người dùng và gọi hàm ratebased
    city = 'london'
    
    output = citybased(city)
    print(output)
    # Trả kết quả về template hoặc API response
    return render(request, 'home.html')

def recommend_hotel_by_city_feature(request):
    city = "london"
    number = 4
    features = 'I need a room with free wifi'
    output = random_forest_based(city, number, features)
    print(output)
    return render(request, 'home.html')
