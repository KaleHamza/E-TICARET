
import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .forms import CustormerForm,ProductForm
from .models import Product,Category
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm

from django.template import Context
# Create your views here.

def index(request):
    # template = loader.get_template('ticaretSitesi/index.html')
    # return HttpResponse(template.render())
    #list comphension
    products = Product.objects.filter(stock__lt=10)
    lowPriceProducts = Product.objects.filter(price__lt=3000)
    categories = Category.objects.all()

    return render(request, 'ticaretSitesi/index.html', {
                  'categories': categories,
                  "products": products,
                  "lowprices":lowPriceProducts
                  })

def product(request):
    product_category = get_object_or_404(Category, categoryName="Product")
    products = Product.objects.filter(category__categoryName=product_category)
    categories = Category.objects.filter(Q(categoryName="Telephone")|Q(categoryName="E-Commarce Table")|
                                         Q(categoryName="E-Commarce Clock")|Q(categoryName="E-Commarce Tshirt"))
    
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })
def electronic(request):
    electronic_category = get_object_or_404(Category, categoryName="Electronic")
    products= Product.objects.filter(category__categoryName=electronic_category)
    categories = Category.objects.filter(Q(categoryName="Telephone")|Q(categoryName="Computer")|
                                         Q(categoryName="Freezer")|Q(categoryName="Hair Dryer"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def personalcare(request):
    personalcare_category = get_object_or_404(Category, categoryName="PersonalCare")
    products= Product.objects.filter(category__categoryName=personalcare_category)
    categories = Category.objects.filter(Q(categoryName="Shaving Machine")|Q(categoryName="rechargeable toothbrush")|
                                         Q(categoryName="hair straightener")|Q(categoryName="Hair Dryer"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def computer(request):
    computer_category = get_object_or_404(Category, categoryName="computer")
    products= Product.objects.filter(category__categoryName=computer_category)
    categories = Category.objects.filter(Q(categoryName="Monitor")|Q(categoryName="Keyboard")|
                                         Q(categoryName="Mouse")|Q(categoryName="Airpod"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def hobbies(request):
    hobbies_category = get_object_or_404(Category, categoryName="hobbies")
    products= Product.objects.filter(category__categoryName=hobbies_category)
    categories = Category.objects.filter(Q(categoryName="Drone")|Q(categoryName="Gym Equipment")|
                                         Q(categoryName="Scooter")|Q(categoryName="Game consol"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def signup(request):
    if request.method == "POST":
        form = CustormerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustormerForm()
    return render(request, "ticaretSitesi/signup.html", {"form":form})

sistemeGiris=False
def login(request):
    if request.method == 'POST':
        form = CustormerForm(request.POST)
        if form.is_valid():
            qs = Customer.objects.values_list("email","password")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            for i in qs:
                if(i[0]==email and i[1]==password):
                    global sistemGiris
                    sistemeGiris=True
                    return redirect('/')
            
    else:
        form = CustormerForm()
    
    return render(request, 'ticaretSitesi/login.html', {'form': form})

def productsDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        print(product.stock)
        product.stock-=1
        print("sonra",product.stock)
        product.save()
        return redirect('/')

        
    context = {
        'product': product
    }
    return render(request, 'ticaretSitesi/details.html', context)

def about(request):
    return render(request, 'ticaretSitesi/about.html')

def basket(request):
    #if request.method == 'POST':
     #   form=ProductForm(request.POST)
      #  print(form)
       # if form.is_valid():
        #    a =form.cleaned_data['title']
         #   print(a)
          #  print("sonra",product.title)
           # #product.title = a
            
            #return redirect('/')
        #else:
         #   print("elsedeyim")
          #  form = ProductForm()
    
    #return render(request, 'basket.html', {'form': form})
    return render(request, 'ticaretSitesi/basket.html')


def getProductByCategory(request, slug):
    products = Product.objects.filter(category__slug=slug).order_by("title")
    categories = Category.objects.all()

    paginator = Paginator(products, 4)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(request, 'ticaretSitesi/list.html', {
        'category': categories,
        'page_obj': page_obj,
        'selectedCategory':slug
    })

