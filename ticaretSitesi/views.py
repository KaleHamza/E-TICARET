from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Product,Category
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

def productsDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'ticaretSitesi/details.html', context)