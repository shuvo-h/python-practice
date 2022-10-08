from django.urls import path
from . import views  # dot means current directory
'''
All Products start with '/products', so we have to tell the path function as the current path
/products
/products/1/details
/products/new
'''

urlpatterns = [
    path('',views.index),
    path('new',views.newFn)
]