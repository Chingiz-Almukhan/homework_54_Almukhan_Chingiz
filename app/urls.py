from django.urls import path

from app.views import index_view, product_view

urlpatterns = [
    path('', index_view, name='main'),
    path('products/<int:pk>', product_view, name='product'),
]