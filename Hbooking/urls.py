
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#admin.site.site_header = 'Medical Appointment '
#admin.site.site_title = 'MedicalAppointment '
#admin.site.index_title = 'Appointment Administration'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
