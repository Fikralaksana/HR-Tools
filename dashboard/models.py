from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class UserEkstention(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departement= models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class Contract(models.Model):
    contract_type=models.CharField(max_length=100)
    def __str__(self):
        return self.contract_type
class Employee(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField(default=date(1960,1,1))
    email=models.EmailField(max_length=100)
    phone_number=PhoneNumberField()
    address=models.TextField(max_length=500)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    contract_type=models.ForeignKey(Contract, on_delete=models.CASCADE)
    contract_start=models.DateField()
    contract_end=models.DateField(blank=True, null=True)
    photo=models.ImageField(upload_to='photo_profil')
    description=models.TextField(max_length=1000)