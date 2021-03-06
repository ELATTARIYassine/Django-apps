from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
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

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form})