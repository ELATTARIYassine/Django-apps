from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    return render(request, "shop/index.html", context={'products': products})