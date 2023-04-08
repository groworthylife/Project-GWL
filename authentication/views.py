from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import *

context = {}

@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def SignUp(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            age = request.POST.get('age')
            phone = request.POST.get('phone')
            std = request.POST.get('std')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if CustomerModel.objects.filter(email=email).first():
                messages.info(request, 'This account already exist. Try logging in.')
                return redirect('login')
            else:
                new_customer = CustomerModel.objects.create(
                    name = name,
                    email = email, 
                    phone = phone,
                    age = age,
                    standerd = std
                )
                new_customer.set_password(password)
                new_customer.save()
                messages.info(request, 'Account Created')
                return redirect('login')         
    except Exception as e:
        print(e)
        messages.error(request, str(e))
    return render(request, "registration.html", context)


def LogIn(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            customer_obj = CustomerModel.objects.filter(email=email).first()
            if customer_obj is None:
                messages.info(request, 'User does not exists. Please Signup')
                return redirect('register')
            user = authenticate(email=email, password=password)
            if user is  None:
                messages.info(request, 'Incorrect Password.')
                return redirect('login')
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('avatar')
    except Exception as e:
        print(e)
        messages.error(request, str(e))
    return render(request, "Sign-in.html", context)


def accountsPage(request):
    return render(request, "accounts.html", context)
