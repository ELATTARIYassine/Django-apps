from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.all()

    #search code
    itemName = request.GET.get('item_name')
    if itemName != "" and itemName is not None:
        products = products.filter(title__contains=itemName)

    #pagination code
    paginator = Paginator(products,4)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    return render(request, "shop/index.html", context={'products': products})

def details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "shop/details.html", context={'product': product})

def checkout(request):
    return render(request, "shop/checkout.html")