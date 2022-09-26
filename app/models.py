from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)
    description = models.CharField(verbose_name='Описание', max_length=15, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    cost = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2)
    image = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)

    def __str__(self):
        return f'{self.name} - {self.cost}'


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, db_index=True)

    def __str__(self):
        return self.name
