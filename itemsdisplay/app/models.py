from django.db import models

# Create your models here.
class Items(models.Model):
    Idno=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=30, decimal_places=3)
    Quantity = models.IntegerField()
    Image = models.ImageField(upload_to='pic')

class Register(models.Model):
    Name = models.CharField(max_length=50, primary_key=True)
    Contact = models.IntegerField()
    Password = models.CharField(max_length=50)
