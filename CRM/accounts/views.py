from django.shortcuts import render
from accounts.models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    totalOrders = Order.objects.count()
    deliveredOrders = Order.objects.filter(status='Delivered').count()
    pendingOrders = Order.objects.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'totalOrders': totalOrders, 'deliveredOrders': deliveredOrders, 'pendingOrders': pendingOrders}
    return render(request, 'accounts/dashboard.html',context=context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk_customer):
    customer = Customer.objects.get(id=pk_customer)
    orders = customer.order_set.all()
    totalOrdersCount = orders.count()
    context = {'customer':customer, 'orders':orders, 'totalOrdersCount': totalOrdersCount}
    return render(request, 'accounts/customer.html', context=context)
