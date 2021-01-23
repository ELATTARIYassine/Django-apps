from django.shortcuts import render,redirect
from accounts.models import *
from .forms import OrderForm

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

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)