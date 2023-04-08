from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .validators import *
from .threads import *
from .models import *
import uuid

context = {}


@login_required(login_url='../login/')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def SignUp(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            age = int(request.POST.get('age'))
            phone = request.POST.get('phone')
            std = request.POST.get('std')
            email = request.POST.get('email')
            password = request.POST.get('password')
            # validate credentials
            if not validate_email(email):
                messages.info(request, 'Invalid Email')
                return redirect('register')
            elif not validate_name(name):
                messages.info(request, 'Invalid Name')
                return redirect('register')
            elif not validate_phone_no(phone):
                messages.info(request, 'Invalid Phone Number')
                return redirect('register')
            elif not validate_age(age):
                messages.info(request, 'Invalid Age')
                return redirect('register')
            elif not validate_standerd(std):
                messages.info(request, 'Select Standerd')
                return redirect('register')

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



def Forget(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            user = CustomerModel.objects.get(email=email)
            if not user:
                messages.info(request, 'This user does not exist. Please Signup.')
                return redirect('/signup')
            token = str(uuid.uuid4())
            user.token = token
            thread_obj = send_forgot_link(email, token)
            thread_obj.start()
            user.save()
            messages.info(request, 'We have sent you a link to reset password via mail')
    except Exception as e:
        print(e)
        messages.error(request, str(e))
    return render(request, "accounts/forgot.html", context)


def Reset(request, token):
    try:
        customer_obj = CustomerModel.objects.get(token=token)
        if not customer_obj:
            messages.info(request, 'This user does not exist. Please Signup.')
            return redirect('/signup')
        if request.method == 'POST':
            npw = request.POST.get('npw')
            cpw = request.POST.get('cpw')
            if npw == cpw:
                customer_obj.set_password(cpw)
                customer_obj.save()
                messages.info(request, 'Password Changed successfully.')
                return redirect('/login')
            messages.error(request, 'New Password and Confirm Password dont match.')
            return redirect('/login')
    except Exception as e :
        print(e)
        messages.error(request, str(e))
    return render(request, "accounts/reset.html", context)
