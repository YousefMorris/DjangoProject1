from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
# Creating a list of products
products = [
    {'id':1,'name':'Television','path':'television.jpg','categoryimagepath':'electronics.jpeg'},
    {'id':2,'name':'banana','path':'banana.webp','categoryimagepath':'fruits.jpeg'},
    {'id':3,'name':'Fridge','path':'fridge.jpg','categoryimagepath':'electronics.jpeg'},
    {'id':4,'name':'Phone','path':'phone.webp','categoryimagepath':'phonescategory.webp'},
]


# Create your views here.
def productdetails(request,productid):
    # productfilter=filter(lambda t:t['id']==productid,products)
    # productfilter=list(productfilter)
    # if productfilter:
    #     return HttpResponse(productfilter)
    # else:
    #     return HttpResponse('<h3>product not found</h3>')

    #get product details by id
    obj1=Product.objects.get(id=productid)
    context={'productdetails':obj1}
    return render(request,'productdetails.html',context)

def product(request):
    # first way from the list
    
    # context={}
    # context['products']=products
    # return render(request,'index.html',context)

    #second way from the DB select statement
    context={'products':Product.objects.all()}
    return render(request,'index.html',context)
def category(request):
    context={}
    context['products']=products
    return render(request,'category.html',context)

def aboutus(request):
    return render(request,'aboutus.html')

def productadd(request):
    if(request.method=='POST'):
        #data recieved from the client side
        #create object product
        Product.objects.create(name=request.POST["tname"],price=int(request.POST["tprice"]))
        return HttpResponseRedirect("/")
    return render(request,'add.html')
def productdelete(request,pID):
    Product.objects.filter(id=pID).delete()
    return HttpResponseRedirect("/")
def productupdate(request,pID):
    if(request.method=='POST'):
        #data recieved from the client side
        #create object product
        Product.objects.filter(id=pID).update(name=request.POST["tname"],price=int(request.POST["tprice"]))
        return HttpResponseRedirect("/")
    context ={'oldData':Product.objects.get(id=pID)}
    return render(request,'update.html',context)