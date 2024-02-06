from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
from .forms import *
from django.views import View
from django.views.generic import UpdateView, DetailView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Creating a list of products
products = [
    {'id':1,'name':'Television','path':'television.jpg','categoryimagepath':'electronics.jpeg'},
    {'id':2,'name':'banana','path':'banana.webp','categoryimagepath':'fruits.jpeg'},
    {'id':3,'name':'Fridge','path':'fridge.jpg','categoryimagepath':'electronics.jpeg'},
    {'id':4,'name':'Phone','path':'phone.webp','categoryimagepath':'phonescategory.webp'},
]


# Create your views here.

# def productdetails(request,productid):
    # productfilter=filter(lambda t:t['id']==productid,products)
    # productfilter=list(productfilter)
    # if productfilter:
    #     return HttpResponse(productfilter)
    # else:
    #     return HttpResponse('<h3>product not found</h3>')

    #get product details by id
    # obj1=Product.objects.get(id=productid)
    # context={'productdetails':obj1}
    # return render(request,'ecommerceapp/productdetails.html',context)

# def product(request):
    # first way from the list
    
    # context={}
    # context['products']=products
    # return render(request,'ecommerceapp/index.html',context)
def product(request):
    #second way from the DB select statement
    context={'products':Product.objects.all()}
    return render(request,'ecommerceapp/index.html',context)

def category(request):
    context={}
    context={'products':Product.objects.all()}
    return render(request,'ecommerceapp/category.html',context)

def aboutus(request):
    return render(request,'ecommerceapp/aboutus.html')
#-----------------first way
# def productadd(request):
#     form = productForm()
#     context={ 'form' : form}
#     if(request.method == 'POST'):
#         #data recieved from the client side
#         #create object product
#         form=productForm(request,request.POST,request.FILES)
#         if form.is_valid:
#             Product.objects.create(
#                 name=request.POST["name"],
#                 price=int(request.POST["price"]),
#                 image=request.FILES["image"],
#                 category=Category.objects.get(id=request.POST["category"]))
#             return HttpResponseRedirect("/")
#         else:
#             context['message'] = "Your Data is not completed"

#     return render(request,'ecommerceapp/add.html',context)

#--------------------------second way using the ModelForm

def productadd(request):
    form = productForm()
    context={ 'form' : form}
    if(request.method == 'POST'):
        #data recieved from the client side
        #create object product
        form=productForm(request.POST,request.FILES)
        if form.is_valid:
            obj=form.save()
            return HttpResponseRedirect("/")
        else:
            context['message'] = "Your Data is not completed"

    return render(request,'ecommerceapp/add.html',context)



def categoryadd(request):
    form = categoryForm()
    context={ 'form' : form}
    if(request.method == 'POST'):
        #data recieved from the client side
        #create object product
        form=categoryForm(request,request.POST,request.FILES)
        if form.is_valid:
            Category.objects.create(
                name=request.POST["name"],
                categoryimage=request.FILES["categoryimage"])
            return HttpResponseRedirect("/")
        else:
            context['message'] = "Your Data is not completed"

    return render(request,'ecommerceapp/add.html',context)



    # if(request.method=='POST'):
    #     #data recieved from the client side
    #     #create object product
    #     Product.objects.create(name=request.POST["tname"],price=int(request.POST["tprice"]),image=request.FILES["timage"])
    #     return HttpResponseRedirect("/")
    # return render(request,'add.html')

def productdelete(request,pID):
    Product.objects.filter(id=pID).delete()
    return HttpResponseRedirect("/")

#---update using a class
class ProductUpdate(View):
    def get(self,request,pID):
        context={ 'form' : productForm(instance=Product.products_details(pID))}
        return render(request,'ecommerceapp/update.html',context)

    def post(self,request,pID):
        form=productForm(request.POST,instance=Product.products_details(pID))
        if form.is_valid:
            obj=form.save()
            return HttpResponseRedirect("/")
    

#def productupdate(request,pID):

    #-------------------first way

    # context={}
    # if request.method=='POST':
    #     #data recieved from the client side
    #     #create object product
    #     #price is casting integer raise an error do not miss it
    #     if request.POST['tname']!="" or request.POST['tprice']!="": 
    #         Product.objects.filter(id=pID).update(name=request.POST["tname"],price=int(request.POST["tprice"]))
    #         return HttpResponseRedirect("/")
    #     else:
            
    #         context['message'] = 'kindly fill all the fields'
    # context['oldData'] = Product.objects.get(id=pID)
    # return render(request,'ecommerceapp/update.html',context)
           
    #---------------------------second way using ModelForm
    
    # context={ 'form' : productForm(instance=Product.products_details(pID))}
    # if request.method=='POST':
    #     form=productForm(request.POST,instance=Product.products_details(pID))
    #     if form.is_valid:
    #         obj=form.save
    #         return HttpResponseRedirect("/")

    # return render(request,'ecommerceapp/update.html',context)
        


#----- update using the generic class

class productUpdategeneric(UpdateView):
    model=Product
    template_name='ecommerceapp/update.html'
    context_object_name='form'
    form_class=productForm 
    success_url=reverse_lazy('productlist')
 
class productShowDetailsgeneric(DetailView):
    model=Product
    template_name='ecommerceapp/productdetails.html'
    context_object_name='productdetails'

class productDeletegeneric(DeleteView):
    model=Product
    template_name='ecommerceapp/productdelete.html'  
    success_url=reverse_lazy('productlist')

class productlistgeneric(ListView):
    model=Product
    template_name='ecommerceapp/index.html'
    context_object_name='products'

class productAddgeneric(CreateView):
    model=Product
    form_class=productForm 
    template_name='ecommerceapp/add.html'
    success_url=reverse_lazy("products")


    
    
 