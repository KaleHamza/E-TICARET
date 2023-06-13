from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('indexadmin', views.indexadmin, name="indexadmin"),
    path('search',views.search, name="search"),
    path('products', views.product, name="product"),
    path('productsadmin', views.productadmin, name="productadmin"),
    path('elektronics', views.electronic, name="electronic"),
    path('elektronicsadmin', views.electronicadmin, name="electronicadmin"),
    path('personalcare', views.personalcare, name="personalcare"),
    path('personalcareadmin', views.personalcareadmin, name="personalcare"),
    path('computer', views.computer, name="computer"),
    path('computeradmin', views.computeradmin, name="computer"),
    path('hobbies', views.hobbies, name="hobbies"),
    path('hobbiesadmin', views.hobbiesadmin, name="hobbies"),
    path('signup', views.signup, name="signup"),
    path('login', views.login,name='login'),
    path('about',views.about,name='about'),
    path('basket',views.basket,name='basket'),
    path('news',views.news,name='news'),
    path('<slug:slug>', views.productsDetail, name="product_details"),
    path('category/<slug:slug>', views.getProductByCategory, name = 'products_by_category'),
    path('category/admin/<slug:slug>', views.getProductByCategoryadmin, name = 'products_by_category_admin'),
]