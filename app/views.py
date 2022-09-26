from django.shortcuts import render, redirect

from app.models import Product, Category


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


def add_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'add_product.html', context)


def add(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    cost = request.POST.get('cost')
    image = request.POST.get('image')
    category = request.POST.get('category')
    product = Product.objects.create(name=name, description=description, cost=cost, image=image, category_id=category)
    return redirect('product', pk=product.pk)


def category_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'add_category.html', context)


def confirm_add(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    category = Category.objects.create(name=name, description=description)
    return redirect('main')
