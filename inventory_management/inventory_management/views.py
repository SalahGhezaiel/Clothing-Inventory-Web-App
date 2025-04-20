from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ClothingItem
from .forms import ClothingItemForm
from django.db.models import Q

@login_required
def clothing_list(request):
    query = request.GET.get('q')
    if query:
        items = ClothingItem.objects.filter(name__iexact=query)
    else:
        items = ClothingItem.objects.all()
    return render(request, 'inventory/clothing_list.html', {'items': items, 'query': query})

@login_required
def clothing_create(request):
    if request.method == 'POST':
        form = ClothingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clothing_list')
    else:
        form = ClothingItemForm()
    return render(request, 'inventory/clothing_form.html', {'form': form})

@login_required
def clothing_update(request, pk):
    item = get_object_or_404(ClothingItem, pk=pk)
    if request.method == 'POST':
        form = ClothingItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('clothing_list')
    else:
        form = ClothingItemForm(instance=item)
    return render(request, 'inventory/clothing_form.html', {'form': form})

@login_required
def clothing_delete(request, pk):
    item = get_object_or_404(ClothingItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('clothing_list')
    return render(request, 'inventory/clothing_confirm_delete.html', {'item': item})
