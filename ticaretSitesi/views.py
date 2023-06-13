from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CustormerForm,CustormerSignUpForm,ProductCreateForm
from .models import Product,Category,AktifKullanici
from .models import Customer
from django.shortcuts import render, redirect
from django.conf import settings
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
def indexadmin(request):
    products = Product.objects.filter(stock__lt=10)
    lowPriceProducts = Product.objects.filter(price__lt=3000)
    categories = Category.objects.all()

    return render(request, 'ticaretSitesi/indexAdmin.html', {
                  'categories': categories,
                  "products": products,
                  "lowprices":lowPriceProducts
                  })
##################################### PRODUCT
def product(request):
    product_category = get_object_or_404(Category, categoryName="Product")
    products = Product.objects.filter(category__categoryName=product_category)
    categories = Category.objects.filter(Q(categoryName="Telephone")|Q(categoryName="E-Commarce Table")|
                                         Q(categoryName="E-Commarce Clock")|Q(categoryName="E-Commarce Tshirt"))
    
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def productadmin(request):
    product_category = get_object_or_404(Category, categoryName="Product")
    products = Product.objects.filter(category__categoryName=product_category)
    categories = Category.objects.filter(Q(categoryName="Telephone")|Q(categoryName="E-Commarce Table")|
                                         Q(categoryName="E-Commarce Clock")|Q(categoryName="E-Commarce Tshirt"))
    
    return render(request, 'ticaretSitesi/productsadmin.html', {
                  'categories': categories,
                  "products": products
                  })

##################################### ELECTRONIC
def electronic(request):
    electronic_category = get_object_or_404(Category, categoryName="Electronic")
    products= Product.objects.filter(category__categoryName=electronic_category)
    categories = Category.objects.filter(Q(categoryName="Telephone")|Q(categoryName="Computer")|
                                         Q(categoryName="Freezer")|Q(categoryName="Hair Dryer"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def electronicadmin(request):
    electronic_category = get_object_or_404(Category, categoryName="Electronic")
    products= Product.objects.filter(category__categoryName=electronic_category)
    categories = Category.objects.filter(Q(categoryName="Telephone")|Q(categoryName="Computer")|
                                         Q(categoryName="Freezer")|Q(categoryName="Hair Dryer"))
    return render(request, 'ticaretSitesi/productsadmin.html', {
                  'categories': categories,
                  "products": products
                  })



##################################### PERSONAL CARE

def personalcare(request):
    personalcare_category = get_object_or_404(Category, categoryName="PersonalCare")
    products= Product.objects.filter(category__categoryName=personalcare_category)
    categories = Category.objects.filter(Q(categoryName="Shaving Machine")|Q(categoryName="rechargeable toothbrush")|
                                         Q(categoryName="hair straightener")|Q(categoryName="Hair Dryer"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def personalcareadmin(request):
    personalcare_category = get_object_or_404(Category, categoryName="PersonalCare")
    products= Product.objects.filter(category__categoryName=personalcare_category)
    categories = Category.objects.filter(Q(categoryName="Shaving Machine")|Q(categoryName="rechargeable toothbrush")|
                                         Q(categoryName="hair straightener")|Q(categoryName="Hair Dryer"))
    return render(request, 'ticaretSitesi/productsadmin.html', {
                  'categories': categories,
                  "products": products
                  })

##################################### COMPUTER
def computer(request):
    computer_category = get_object_or_404(Category, categoryName="computer")
    products= Product.objects.filter(category__categoryName=computer_category)
    categories = Category.objects.filter(Q(categoryName="Monitor")|Q(categoryName="Keyboard")|
                                         Q(categoryName="Mouse")|Q(categoryName="Airpod"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def computeradmin(request):
    computer_category = get_object_or_404(Category, categoryName="computer")
    products= Product.objects.filter(category__categoryName=computer_category)
    categories = Category.objects.filter(Q(categoryName="Monitor")|Q(categoryName="Keyboard")|
                                         Q(categoryName="Mouse")|Q(categoryName="Airpod"))
    return render(request, 'ticaretSitesi/productsadmin.html', {
                  'categories': categories,
                  "products": products
                  })

##################################### Hobbies
def hobbies(request):
    hobbies_category = get_object_or_404(Category, categoryName="hobbies")
    products= Product.objects.filter(category__categoryName=hobbies_category)
    categories = Category.objects.filter(Q(categoryName="Drone")|Q(categoryName="Gym Equipment")|
                                         Q(categoryName="Scooter")|Q(categoryName="Game consol"))
    return render(request, 'ticaretSitesi/products.html', {
                  'categories': categories,
                  "products": products
                  })

def hobbiesadmin(request):
    hobbies_category = get_object_or_404(Category, categoryName="hobbies")
    products= Product.objects.filter(category__categoryName=hobbies_category)
    categories = Category.objects.filter(Q(categoryName="Drone")|Q(categoryName="Gym Equipment")|
                                         Q(categoryName="Scooter")|Q(categoryName="Game consol"))
    return render(request, 'ticaretSitesi/productsadmin.html', {
                  'categories': categories,
                  "products": products
                  })

##################################### Sign Up
def signup(request):
    if request.method == "POST":
        form = CustormerSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustormerSignUpForm()
    return render(request, "ticaretSitesi/signup.html", {"form":form})

##################################### Login
def login(request):
    if request.method == 'POST':
        form = CustormerForm(request.POST)
        if form.is_valid():
            qs = Customer.objects.values_list("email","password")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            for i in qs:
                if(i[0]==email and i[1]==password):
                    print(i[0],i[1])
                    aktif_kullanici_secenegi = AktifKullanici()
                    print("tablo boş:",aktif_kullanici_secenegi.email)
                    aktif_kullanici_secenegi.email = i[0]
                    print("tablodaki mail:",aktif_kullanici_secenegi.email)
                    aktif_kullanici_secenegi.save()
                    print("saveden sonra",aktif_kullanici_secenegi)

                    return redirect('/indexadmin')
            
    else:
        form = CustormerForm()
    
    return render(request, 'ticaretSitesi/login.html', {'form': form})

##################################### Product Detail
def productsDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        #Aktif mail adresini alıp ürünü o kişiye ekleyeceğiz
        #aktif_kullanici_mail=AktifKullanici()
        #mail=aktif_kullanici_mail[0].email
        #Datadan şu andaki kullanıcının verilerine eriştik
        #customer=Customer.objects.filter(Q(email=mail))
        #Kullanıcının sepetine ürünü ekledik.
        #customer.basket["tutacak"]=product.title
        #customer.save()
        #Ürünü bir azalttık
        product.stock-=1
        product.save()
        return redirect('/')
    context = {
        'product': product
    }
    return render(request, 'ticaretSitesi/details.html', context)

##################################### About
def about(request):
    return render(request, 'ticaretSitesi/about.html')

##################################### Basket
def basket(request):
            #Aktif mail adresini alıp ürünü o kişiye ekleyeceğiz
        # aktif_kullanici_mail=AktifKullanici()
        # mail=aktif_kullanici_mail[0].email
        # print("aktif mail:",aktif_kullanici_mail.email)
            # #Datadan şu andaki kullanıcının verilerine eriştik
        # customer=Customer(Q(email=mail))
        # print("aktif customer:",customer)
        # basket=customer.basket
        # print("sepetimiz:",basket),{"basket":basket}
    return render(request, 'ticaretSitesi/basket.html')

##################################### Search
def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        products = Product.objects.filter(title__contains=q).order_by("price")
        print(products)
        categories = Category.objects.all()
    else:
        return redirect("/products")
    
    

    return render(request, 'ticaretSitesi/search.html', {
        'categories': categories,
        'products': products,
    })
##################################### Get Product by category
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

def getProductByCategoryadmin(request, slug):
    products = Product.objects.filter(category__slug=slug).order_by("title")
    categories = Category.objects.all()

    paginator = Paginator(products, 4)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(request, 'ticaretSitesi/listadmin.html', {
        'category': categories,
        'page_obj': page_obj,
        'selectedCategory':slug
    })

def news(request):
    if request.method == "POST":
        form = ProductCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/indexadmin")
    else:
        form = ProductCreateForm()
    return render(request, "ticaretSitesi/news.html", {"form":form})
