from django import forms
from .models import *
from django.core.exceptions import ValidationError


class productForm(forms.Form):
    name=forms.CharField(max_length=20,required=True)
    price=forms.IntegerField(required=True)
    image=forms.ImageField(required=True)
    category=forms.ChoiceField(choices=Category.getCategory())
    def clean_name(self):
        enteredname=self.cleaned_data['name']
        obj=Product.objects.get(name=enteredname).exists()
        if obj:
            raise ValidationError('name must be unique')
        else:
            return True
        
#category form
class categoryForm(forms.Form):
    name=forms.CharField(max_length=20,required=True)
    categoryimage=forms.ImageField(required=True)
    # def clean_name(self):
    #     enteredname=self.cleaned_data['name']
    #     obj=Product.objects.get(name=enteredname).exists()
    #     if obj:
    #         raise ValidationError('name must be unique')
    #     else:
    #         return True                
    