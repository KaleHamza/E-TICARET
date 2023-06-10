from django.contrib import admin

from .models import Category, Customer, Product

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username","surname","password","email", "phone","Current","adresses")
admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin): 
    list_display = ("title","description","color","imageUrl", "price","stock","category")
    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html+= category.name+" "
        return html
admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryName",)
    def course_count(self, obj):
        return obj.course_set.count()
admin.site.register(Category,CategoryAdmin)

