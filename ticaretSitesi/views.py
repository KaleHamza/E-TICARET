from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import CustormerForm
from .models import Product,Category
from .models import Customer
# Create your views here.
def index(request):
    # template = loader.get_template('ticaretSitesi/index.html')
    # return HttpResponse(template.render())

    #list comphension
    products = Product.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'ticaretSitesi/index.html', {
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

def login(request):
    if request.method == "POST":
        form = CustormerForm(request.POST)

        #if form.is_valid():
        #testemail=request.POST["email"]
        testemail=request.POST.get('email', False)
        testpassword=request.POST.get('password', False)
        for i in Customer:
            email = Customer[i].email
            password = Customer[i].password
            if(testemail==email & testpassword == password):
                return redirect("/")
        #else:
        #print("Test başarısız")
    else:
        form = CustormerForm()
    return render(request, "ticaretSitesi/login.html", {"form":form})

def productsDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'ticaretSitesi/details.html', context)
