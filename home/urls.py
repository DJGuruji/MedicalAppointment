
from django.urls import path
from .import views
urlpatterns = [
  
path('',views.register, name ='register'),
path('home',views.index, name ='home'),
path('login',views.user_login, name ='login'),

path('about',views.about, name ='about'),
path('booking',views.booking, name ='booking'),
path('contact',views.contact, name ='contact'),
path('doctors',views.doctors, name ='doctors'),
path('logout',views.logout_user, name ='logout'),
  
]