from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from main.models import Item
# Create your views here.

def homepage(request):
    return render(request, template_name='main/home.html')

def itemspage(request):
    items = Item.objects.all()
    return render(request, template_name='main/items.html', context={'items': items})

def loginpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('items')
        else:
            return redirect('login')

def registerpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/register.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')

def logoutpage(request):
    logout(request)
    return redirect('home')