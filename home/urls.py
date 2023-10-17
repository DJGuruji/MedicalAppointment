from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  
path('',views.register, name ='register'),
path('home',views.index, name ='home'),
path('login',views.user_login, name ='login'),
path('about',views.about, name ='about'),
path('appointment',views.appointments, name='appointment'),
path('booking',views.booking, name ='booking'),
path('contact',views.contact, name ='contact'),
path('doctors',views.doctors, name ='doctors'),
path('delete/<pk>',views.delete, name='delete'),
path('logout',views.logout_user, name ='logout'),

path('reset_pass',auth_views.PasswordResetView.as_view(template_name = "passwordreset.html"), name='reset_pass'),
path('reset_pass_sent',auth_views.PasswordResetDoneView.as_view(template_name = "passwordresetsent.html"), name='reset_pass_sent'),
path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = "passwordresetform.html"), name='password_reset_confirm'),
path('reset_pass_comp',auth_views.PasswordResetCompleteView.as_view(template_name = "passwordresetdone.html"), name='reset_pass_comp'),
  
]