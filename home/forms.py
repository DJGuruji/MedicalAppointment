
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking
import datetime
class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
  

class DateInput(forms.DateInput):
  input_type = 'date'
class TimeInput(forms.TimeInput):
  input_type = 'time'
    
class Bookingform(forms.ModelForm):
  class Meta:
    model = Booking
    fields = '__all__'
    
    widgets = {
      'booking_date' : DateInput(attrs={'min': datetime.date.today() }),
      'booking_time' : TimeInput(attrs={'min': '8', 'max': '17'})
      
    }
    
    labels = {
      'p_name' : 'Patient Name',
      'p_phone' : 'Patient Phone',
      'p_email' : 'Patient Email',
      'doc_name' : 'Choose Doctor',
      'booking_date' : 'Choose Date',
      'booking_time':'Choose Time'
      
    }
    
    
    