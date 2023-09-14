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
