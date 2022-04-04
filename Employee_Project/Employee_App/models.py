from django.db import models

# Create your models here.
class Employee(models.Model):
    empID = models.IntegerField(primary_key=True,unique=True)
    empName = models.CharField(max_length=5000)
    empDOJ = models.DateField(auto_now_add=True)
    empDescription = models.CharField(max_length=5000)
    empCategory = models.CharField(max_length=5000)
    empCity = models.CharField(max_length=5000)
    empOfficeVenue = models.CharField(max_length=5000)

    def __str__(self) :
        return self.empName