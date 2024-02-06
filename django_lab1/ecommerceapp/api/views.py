from rest_framework import views,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ecommerceapp.models import *
from .seralizer import *

@api_view(['GET'])
def Printallproducts(request):
    data=Product.objects.all()
    datajson=Productseralizer(data,many=True).data
    return Response({'data':datajson})
@api_view(['GET'])
def getproduct(request,id):
    productdata=Productseralizer(Product.products_details(id)).data
    return Response({'data':productdata})


@api_view(['GET','POST'])
def addproduct(request):
    # obj=Product()
    # obj.id=request.data['id']
    # obj.name=request.data['name']
    # obj.image=request.data['image']
    # obj.price=request.data['price']
    # obj.createdat=request.data['createdat']
    # obj.updatedat=request.data['updatedat']
    # obj.save()
    obj=Productseralizer(data=request.data)
    if(obj.is_valid()):
        obj.save()
        return Response({'data':"print data"})
    else:
        return Response({'data':"invalid data","obj":obj.errors})


@api_view(['PUT'])
def updateproduct(request,id):
    updateobj=Product.objects.filter(id=id).first()
    if updateobj:
        seralizedproduct=Productseralizer(instance=updateobj,data=request.data)
        if seralizedproduct.is_valid():
            serializers.save()
            return Response(data=seralizedproduct.data)
    return Response({'msg':'product not found'})

@api_view(['DELETE'])
def deleteproduct(request,id):
    trydelete=Product.objects.filter(id=id).first()
    if(trydelete):
        trydelete.delete()
        return Response({'msg':'product deleted'})
    return Response({'msg':'product not found'})
