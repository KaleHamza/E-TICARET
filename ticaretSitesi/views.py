
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .forms import CustormerForm
from .models import Product,Category
from .models import Customer
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

# def login(request):
#     if request.method == "POST":
#         form = CustormerForm(request.POST)
#         print("if e girdi")
#          #if form.is_valid():
#          #testemail=request.POST["email"]
#         testemail = request.POST.get('inputEmail')
#         testpassword = request.POST.get('inputPassword')
#         print("test e mail" ,testemail)
#         print("test password" ,testpassword)
#         for each in Customer.objects.all():
#             print("for e girdi")
#             email=each.email
#             password=each.password
#             print(email)
#             print(password)
#             if(testemail==email and testpassword == password):
#                 print("for un ifine girdi")
#                 return redirect("/")
#          #else:
#          #print("Test başarısız")
#     else:
#         print("else e girdi")
#         form = CustormerForm()
#     return render(request, "ticaretSitesi/login.html", {"form":form})


def login(request):
    
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = CustormerForm(request, data=request.POST)
        if form.is_valid():
            qs = Customer.objects.values_list("email","password")
            testemail=request.POST["id_email"]
            testpassword=request.POST["id_password"]
            for i in qs:
                if(qs[i][0]==testemail and qs[i][1]==testpassword):
                    return redirect('/')
    else:
        form = CustormerForm(request)
    context = {
        "form": form
    }
    return render(request, "ticaretSitesi/login.html", context)


def productsDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'ticaretSitesi/details.html', context)

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
