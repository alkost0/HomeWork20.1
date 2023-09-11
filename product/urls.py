from django.urls import path
from product.apps import ProductConfig
from product.views import index, contacts, category, category_products, product

app_name = ProductConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('<int:pk>/category_products', category_products, name='category_products'),
    path('<int:pk>/product/', product, name='product')
]
