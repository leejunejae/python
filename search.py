from django.shortcuts import render
from django.db.models import F
from products.models import Product

def search(request):
    products = Product.objects.all()
    sdata = request.GET.get('sdata','')

    search = []
    for i in products :
        if sdata == i.brand :
            search.append(i)
        elif sdata == i.category2:
            search.append(i)
        elif sdata == i.category3:
            search.append(i)

    return render(request, 'search.html', { 'products': search})