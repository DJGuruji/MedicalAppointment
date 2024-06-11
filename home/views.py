# Create your views here.
from django.shortcuts import render,redirect
  
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
  
from django.contrib.auth.decorators import login_required ,user_passes_test
  
from django.contrib import messages

from .forms import CreateUserForm,Bookingform
  
from .models import *

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage,EmailMultiAlternatives

from django.views.decorators.cache import never_cache

 
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
                
                subject = 'MEDICAL APPOINTMENT ACCOUNT REGISTRATION'
                message = 'Account Register Confirmation'
                recipient = form.cleaned_data.get('email')
                context = {
                    'user': user
                }
                card_html = render_to_string('registeremail.html', context)
                
                email = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, [recipient])
                email.attach_alternative(card_html, 'text/html')
                email.send(fail_silently=False)
                
                messages.success(request, 'Account created for ' + user)
                return redirect('login')
            else:
                for error in form.errors.values():
                    messages.error(request, error)

        context = {'form': form}
        return render(request, 'register.html', context)


 
  
  
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
      form.instance.user = request.user
      form.save()
      patient = form.cleaned_data.get('p_name')
      booking_date = form.cleaned_data.get('booking_date')
      booking_time = form.cleaned_data.get('booking_time')
      doctor = form.cleaned_data.get('doc_name')
      context = {
       'patient' : patient,
       'booking_time': booking_time,
       'booking_date': booking_date,
       'doctor': doctor
       
      }
      card_html = render_to_string('emailsend.html', context)

      subject = 'MEDICAL APPOINTMENT'
      message = 'Medical Appointment confirmation'
      recepiant = form.cleaned_data.get('p_email')
      #send_mail(subject, message,settings.EMAIL_HOST_USER,[recepiant],html_message=card_html, content_type='text/html',fail_silently=False)
      email = EmailMultiAlternatives(subject, message,settings.EMAIL_HOST_USER, [recepiant])
     
      email.attach_alternative(card_html, 'text/html')
      email.send(fail_silently=False)
        
      return render(request,'confirmation.html',context)
  return render(request, 'booking.html',dict_form)
 


@login_required(login_url ='login') 
def contact(request):
  return render(request, 'contact.html')
 


 

@login_required(login_url ='login') 
def delete(request,pk):
  instance = Booking.objects.get(pk=pk)
  if request.method == 'POST':
    instance.delete()
  
  dict_book = {
    'booking' : Booking.objects.all()
  }
  return render(request,'appointments.html',dict_book)


@login_required(login_url='login')
@never_cache
def deletee(request, pk):
  Booking.objects.get(pk=pk).delete()
  user_bookings = Booking.objects.filter(user=request.user)
  return render(request, 'myappointments.html', {'bookings': user_bookings})



def is_admin(user):
    return user.is_staff  # Assuming staff members are admins

@login_required(login_url ='login') 
@user_passes_test(is_admin, login_url='login')
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
  
  

@login_required(login_url='login')
def myappointments(request):
    user = request.user  # Assuming you are using Django's built-in User model
    user_bookings = Booking.objects.filter(user=user)
    return render(request, 'myappointments.html', {'bookings': user_bookings})
    