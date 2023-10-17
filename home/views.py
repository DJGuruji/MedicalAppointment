# Create your views here.
from django.shortcuts import render,redirect
  
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
  
from django.contrib.auth.decorators import login_required 
  
from django.contrib import messages

from .forms import CreateUserForm,Bookingform
  
from .models import *

from django.core.mail import send_mail
from django.conf import settings

  
def register(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    form = CreateUserForm()
    if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        
        subject = f'MEDICAL APPOINTMENT ACCOUNT REGISTRATION'
        message = 'Thank you {user} for registering! Your account has been successfully created. You can now log in and start exploring our services. If you have any questions or need assistance, feel free to reach out to our support team'
        recepiant = form.cleaned_data.get('email')
        send_mail(subject, message,settings.EMAIL_HOST_USER,[recepiant],fail_silently=False)
        messages.success(request,'success')
      
        messages.success(request,'Account created for '+ user)
        return redirect('login')
  
  context ={ 'form' :form}
  return render(request,'register.html', context)
  
  
  
def user_login(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username = username, password = password)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.success(request,'Invalid Credential')
        return render(request,'login.html')
  
  context = {}
  return render(request,'login.html', context)
  
  
  
def logout_user(request):
  logout(request)
  return redirect('login')
 
@login_required(login_url ='login') 
def index(request):
  dict_dept = {
    'dept' : Department.objects.all()
  }
  return render(request, 'home.html',dict_dept)
  
@login_required(login_url ='login')   
def about(request):
  return render(request, 'about.html')

@login_required(login_url ='login') 
def booking(request):
  form = Bookingform()
  dict_form = {
    'form' : form
  }
  
  if request.method == 'POST':
    form = Bookingform(request.POST)
    if form.is_valid():
      form.save()
      patient = form.cleaned_data.get('p_name')
      booking_date = form.cleaned_data.get('booking_date')
      booking_time = form.cleaned_data.get('booking_time')
      doctor = form.cleaned_data.get('doc_name')
      subject = 'MEDICAL APPOINTMENT'
      message = f'Thank you { patient } for booking your medical appointment on { booking_date } at { booking_time } for  { doctor }. Please arrive 15 minutes early and remember to bring any necessary documentation or insurance cards. If you need to reschedule or have any questions, please contact us at medicalAppointment.com. We look forward to assisting you with your healthcare needs.'
      recepiant = form.cleaned_data.get('p_email')
      send_mail(subject, message,settings.EMAIL_HOST_USER,[recepiant],fail_silently=False)
      context = {
       'patient' : patient,
       'booking_time': booking_time,
       'booking_date': booking_date,
       'doctor': doctor
       
      }
     
      return render(request,'confirmation.html', context)
  return render(request, 'booking.html',dict_form)

@login_required(login_url ='login') 
def contact(request):
  return render(request, 'contact.html')
 
 

@login_required(login_url ='login') 
def delete(request,pk):
  instance = Booking.objects.get(pk=pk)
  instance.delete()
  dict_book = {
    'booking' : Booking.objects.all()
  }
  return render(request,'appointments.html',dict_book)
 
@login_required(login_url ='login') 
def appointments(request):
  dict_book = {
    'booking' : Booking.objects.all()
  }
  return render(request,'appointments.html',dict_book)
 
  
@login_required(login_url ='login') 
def doctors(request):
  dict_dept = {
    'dept' : Doctor.objects.all()
  }
  return render(request, 'doctors.html',dict_dept)