from django.db import models

NULLABLE = {"blank": True, "null": True}

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    descriptions = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='цена за покупку')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name}: {self.descriptions}, {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
#    created_at = models.DateTimeField(auto_now_add=True, verbose_name='когда создан', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
