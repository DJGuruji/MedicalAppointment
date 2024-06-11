
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking
import datetime



class CreateUserForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    widget=forms.PasswordInput(attrs={'id': 'id_password'})

  def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email 
    
  

class DateInput(forms.DateInput):
  input_type = 'date'
class TimeInput(forms.TimeInput):
  input_type = 'time'
    
class Bookingform(forms.ModelForm):
  class Meta:
    model = Booking
   
    exclude = ['user']
    
    widgets = {
      'booking_date' : DateInput(attrs={'min': datetime.date.today() ,}),
      'p_name': forms.TextInput(attrs={'class': 'form-control',}),
      'p_phone': forms.TextInput(attrs={'class': 'form-control',}),
      'doc_name': forms.Select(attrs={'class': 'form-control',}),
      'p_email': forms.EmailInput(attrs={'class': 'form-control',}),
      'booking_time' : TimeInput(attrs={'class':'form-control',}),
      
    }
    
    labels = {
      'p_name' : 'Patient Name',
      'p_phone' : 'Patient Phone',
      'p_email' : 'Patient Email',
      'doc_name' : 'Choose Doctor',
      'booking_date' : 'Choose Date',
      'booking_time':'Choose Time'
      
    }
    
    
    