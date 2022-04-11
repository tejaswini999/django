from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(models.Model):
    empID = models.AutoField(primary_key=True)
    empName = models.CharField(max_length=50,blank=False)
    empDOJ = models.DateField(default=datetime.date.today())
    empDescription = models.CharField(max_length=500) 
    empCategory = models.CharField(max_length=500) 
    empCity = models.CharField(max_length=50,blank=False) 
    empOfficeVenue = models.CharField(max_length=50) 
    
    def __str__(self) :
        return self.empName

class CustomUser( AbstractUser):
    """
    Custom user model that uses email for authentication instead of django default username attribute
    """

    creation_date = None
    name = None
    display_name = models.CharField(('display name'), max_length=150, blank=True)
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "user"
        ordering = ("-date_joined",)
        indexes = (
            models.Index(fields=["display_name"]),
            models.Index(fields=["username"]),
            models.Index(fields=["email"]),
            models.Index(fields=["date_joined"]),
        )

 