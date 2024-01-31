from django.shortcuts import render
from django.http import HttpResponse

# Creating a list of products
products = [
    {'id':1,'name':'Television','path':'television.jpg','categoryimagepath':'electronics.jpeg'},
    {'id':2,'name':'banana','path':'banana.webp','categoryimagepath':'fruits.jpeg'},
    {'id':3,'name':'Fridge','path':'fridge.jpg','categoryimagepath':'electronics.jpeg'},
    {'id':4,'name':'Phone','path':'phone.webp','categoryimagepath':'phonescategory.webp'},
]


# Create your views here.
def productdetails(request,productid):
    productfilter=filter(lambda t:t['id']==productid,products)
    productfilter=list(productfilter)
    if productfilter:
        return HttpResponse(productfilter)
    else:
        return HttpResponse('<h3>product not found</h3>')
def product(request):
    context={}
    context['products']=products
    return render(request,'index.html',context)
def category(request):
    context={}
    context['products']=products
    return render(request,'category.html',context)

def aboutus(request):
    return render(request,'aboutus.html')