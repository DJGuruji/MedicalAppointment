from django.db import models

class Departments(models.Model):
  dep_name = models.CharField(max_length= 100)
  dep_desc = models.TextField()
  
  def __str__(self):
    return self.dep_name
  
  

