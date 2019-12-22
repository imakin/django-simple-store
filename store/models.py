from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Storesetting(models.Model):
    name = models.CharField(max_length=256, primary_key=True, default="unused")
    value = models.TextField(default="")
    #price currency
    #price multiplier

class Product(models.Model):
    enabled = models.BooleanField(default=True)
    sku     = models.CharField(max_length=64, unique=True)
    name    = models.CharField(max_length=200)
    stock   = models.IntegerField(default=0)
    price   = models.IntegerField(default=0)
    description= models.TextField(blank=True, null=True)
    additional_image_links = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    enabled = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=30, unique=True)
    cart = models.ManyToManyField('Product')

class Address(models.Model):
    complete_address = models.TextField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    address = models.TextField()#text copy
    status = models.TextField()
    complete = models.BooleanField(default=False)

    
