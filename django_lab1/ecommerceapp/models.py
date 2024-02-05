from django.db import models

# Create your models here.
#category model
class Category(models.Model):
    name=models.CharField(max_length=100)
    categoryimage=models.ImageField(upload_to='ecommerceapp/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name},{self.categoryimage}"
    @classmethod
    def getCategory(self):
        return [(eachcat.id,eachcat.name)for eachcat in self.objects.all()]

    def getimageurl(self):
        return f'/media/{self.categoryimage}'
    
#product model
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='ecommerceapp/images/', blank=True, null=True)
    price=models.IntegerField(default=0)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    #object of Category model
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name},{self.image},{self.createdat},{self.updatedat}"
    @classmethod
    def products_List(self):
        return self.objects.all()
    @classmethod
    def products_details(cls,pID):
        return cls.objects.get(id=pID)
    def getimageurl(self):
        return f'/media/{self.image}'
     