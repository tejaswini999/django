from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=5000)
    last_name = models.CharField(max_length=5000)
    email = models.EmailField(max_length=5000,unique=True)
    job_role = models.CharField(max_length=5000)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.first_name