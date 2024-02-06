from django.urls import path
from .views import *

urlpatterns=[
    path('hello',Hello,name='hello'),
    path('acceptdata/',acceptdata,name='acceptdata'),
    path('Printallproducts/',Printallproducts,name='Printallproducts'),
    path('getproduct/<int:id>',getproduct,name='getproduct'),
    path('addproduct/',addproduct,name='addproduct'),
    path('updateproduct/<int:id>',updateproduct,name='updateproduct'),
    path('deleteproduct/<int:id>',deleteproduct,name='deleteproduct'),

] 