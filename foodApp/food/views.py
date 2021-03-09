from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, "food/index.html", context=context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/details.html'

class CreateItem(CreateView):
    model = Item
    fields = ['name', 'description', 'price', 'image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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

def update_item(request, pk_item):
    item = Item.objects.get(pk=pk_item)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, pk_item):
    item = Item.objects.get(pk=pk_item)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item': item})