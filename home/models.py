from django.db import models

class Department(models.Model):
  dep_name = models.CharField(max_length= 100)
  dep_desc = models.TextField()
  
  def __str__(self):
    return self.dep_name
  
  
class Doctor(models.Model):
  doc_name = models.CharField(max_length=100)
  doc_spec = models.CharField(max_length=100)
  dep_name = models.ForeignKey(Department,on_delete= models.CASCADE)
  
  def __str__(self):
    return 'Dr.'+self.doc_name+'-('+self.doc_spec+')'


class Booking(models.Model):
  p_name = models.CharField(max_length=100)
  p_phone = models.CharField(max_length=10)
  p_email = models.EmailField()
  doc_name = models.ForeignKey(Doctor, on_delete = models.CASCADE)
  booking_date = models.DateField()
  booked_on = models.DateField(auto_now = True)
  
  def __str__(self):
    return self.p_name