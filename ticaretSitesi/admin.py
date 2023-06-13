from django.contrib import admin

from .models import Category, Customer, Product,AktifKullanici

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username","surname","password","email", "phone","Current","adresses")
admin.site.register(Customer,CustomerAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ("title","description","color","imageUrl", "slug","price","stock","category_list")
    list_display_links=("title","slug")
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title","color")
    read_only_fields = ("slug")
    search_fields = ("title","color")

    def category_list(self, obj):
        html = ""
        for category in obj.category.all():
            html+= category.categoryName+" "
        return html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryName",)
    def course_count(self, obj):
        return obj.course_set.count()
admin.site.register(Category,CategoryAdmin)

@admin.register(AktifKullanici)
class AktifKullaniciAdmin(admin.ModelAdmin):
    list_display = ("email",)

