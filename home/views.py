
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm, Bookingform
from .models import *

  
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
      return render(request,'confirmation.html')
  return render(request, 'booking.html',dict_form)

@login_required(login_url ='login') 
def contact(request):
  return render(request, 'contact.html')
  
@login_required(login_url ='login') 
def doctors(request):
  dict_dept = {
    'dept' : Doctor.objects.all()
  }
  return render(request, 'doctors.html',dict_dept)