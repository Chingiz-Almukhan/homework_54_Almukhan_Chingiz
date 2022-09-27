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
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'add_product.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        cost = request.POST.get('cost')
        image = request.POST.get('image')
        category = request.POST.get('category')
        product = Product.objects.create(name=name, description=description, cost=cost, image=image,
                                         category_id=category)
        return redirect('product', pk=product.pk)


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'add_category.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = Category.objects.create(name=name, description=description)
        return redirect('main')


def edit_view(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'product': product,
                   'categories': categories}
        return render(request, 'edit_view.html', context)
    elif request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.cost = request.POST.get('cost')
        product.image = request.POST.get('image')
        product.save()
        return redirect('main')


def delete_view(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('main')
