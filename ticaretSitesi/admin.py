from django.contrib import admin

from .models import Category, Customer, Product

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username","surname","password","email", "phone","Current","adresses")
admin.site.register(Customer,CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryName",)
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin): 
    list_display = ("title","description","color","imageUrl", "price","stock","category") 
admin.site.register(Product,ProductAdmin)