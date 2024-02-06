from django.urls import path
from ecommerceapp import views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.product),  # to open directly on the products view without any url path
    path("category", views.category),
    path("aboutus", views.aboutus),
    # path("add", views.productadd),
    path("addcategory", views.categoryadd),
    # path('productdetails/<int:productid>', views.productdetails),
    # path('productdelete/<int:pID>', views.productdelete),

    #--- for calling the def productupdate
    #path('productupdate/<int:pID>', views.productupdate,name='product.update'),

    #--- for calling the update class as a view
    #path('productupdate/<int:pID>', views.ProductUpdate.as_view()),

    #--- for calling the update generic class as a view
    path('productupdate/<pk>', views.productUpdategeneric.as_view()),

    #--- for calling the product details using generic class as a view
    path('productdetails/<pk>', views.productShowDetailsgeneric.as_view()),

    #--- for calling the delete product using generic class as a view
    path('productdelete/<pk>', views.productDeletegeneric.as_view(),name="productdelete"),

    #--- for calling the list product using generic class as a view
    path('productlist', views.productlistgeneric.as_view(),name="productlist"),
    
    #--- for calling the list product using generic class as a view
    
    path('add', login_required(views.productAddgeneric.as_view()),name="products"),


    
    # path('new',productadd,name='product.add'),
]