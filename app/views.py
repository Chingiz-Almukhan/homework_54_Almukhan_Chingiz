from django.shortcuts import render

from app.models import Product


def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main_page.html', context)


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })
