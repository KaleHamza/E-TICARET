from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=30)
    Current = models.FloatField()
    adresses = models.CharField(max_length=250)

class Category(models.Model):
    categoryName = models.CharField(max_length=40)
    
class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    color = models.CharField(max_length=20)
    imageUrl = models.CharField(max_length=50, blank=False)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


