from django.urls import path
from ecommerceapp import views
from . import views
urlpatterns = [
    path('<int:productid>', views.productdetails),
]