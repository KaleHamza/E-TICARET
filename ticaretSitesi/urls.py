from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('products', views.product, name="product"),
    path('elektronics', views.electronic, name="electronic"),
    path('personalcare', views.personalcare, name="personalcare"),
    path('computer', views.computer, name="computer"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('signup', views.signup, name="signup"),
    path('login', views.login,name='login'),
    path('<slug:slug>', views.productsDetail, name="product_details"),
     path('category/<slug:slug>', views.getProductByCategory, name = 'products_by_category'),
]