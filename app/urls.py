from django.urls import path

from app.views import index_view, product_view, add_view, add, category_view, confirm_add

urlpatterns = [
    path('', index_view, name='main'),
    path('products/<int:pk>', product_view, name='product'),
    path('products/add', add_view, name='add'),
    path('products/confirm/', add),
    path('categories/add', category_view, name='category_add'),
    path('categories/confirm/', confirm_add),

]