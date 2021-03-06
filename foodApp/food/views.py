from django.shortcuts import render
from .models import Item
# Create your views here.

def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, "food/index.html", context=context)

def item(request):
    return "z"

def detail(request, pk_item):
    item = Item.objects.get(pk=pk_item)
    context = {'item': item}
    return render(request, "food/details.html", context=context)
