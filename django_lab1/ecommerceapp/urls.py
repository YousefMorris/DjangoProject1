from django.urls import path
from ecommerceapp import views
from . import views
urlpatterns = [
    path("", views.product),  # to open directly on the products view without any url path
    path("category", views.category),
    path("aboutus", views.aboutus),
    path("add", views.productadd),
    path('productdetails/<int:productid>', views.productdetails),
    path('productdelete/<int:pID>', views.productdelete),
    path('productupdate/<int:pID>', views.productupdate),
    # path('new',productadd,name='product.add'),
]