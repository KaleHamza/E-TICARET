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

    def __str__(self):
        return f"{self.username}"

class Category(models.Model):
    categoryName = models.CharField(max_length=40)
    slug = models.SlugField(default = "" ,null=False ,unique=True ,db_index=True ,max_length=50)
    
    def __str__(self):
        return f"{self.categoryName}"
    

class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    color = models.CharField(max_length=20)
    imageUrl = models.CharField(max_length=50, blank=False)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(default="", blank=True,null = False, unique=True, primary_key=True)
    
    def __str__(self):
        return f"{self.title}"
