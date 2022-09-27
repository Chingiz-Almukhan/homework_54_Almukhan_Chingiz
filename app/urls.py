from django.urls import path

from app.views import index_view, product_view, add_view, category_view, edit_view, delete_view

urlpatterns = [
    path('', index_view, name='main'),
    path('products/<int:pk>', product_view, name='product'),
    path('products/add', add_view, name='add'),
    path('categories/add', category_view, name='category_add'),
    path('products/<int:pk>/edit', edit_view, name='edit'),
    path('products/<int:pk>/delete', delete_view, name='delete'),

]