from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=200,null=True)
    price=models.IntegerField(default=0)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name},{self.image},{self.createdat},{self.updatedat}"
    