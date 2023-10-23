from django.contrib import admin
from .models import *

class DoctorAdmin(admin.ModelAdmin):
  list_display = ('id','doc_name','doc_spec','dep_name','doc_email','doc_phone')
  
class BookingAdmin(admin.ModelAdmin):
  list_display = ('id','user','p_name','p_phone','p_email','doc_name','booked_on','booking_date','booking_time')
  
admin.site.register(Department)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Booking, BookingAdmin)

