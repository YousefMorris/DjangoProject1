from django import forms
from .models import *
from django.core.exceptions import ValidationError

#--------------------------first way 
# class productForm(forms.Form):
#     name=forms.CharField(max_length=20,required=True)
#     price=forms.IntegerField(required=True)
#     image=forms.ImageField(required=True)
#     category=forms.ChoiceField(choices=Category.getCategory())
#     def clean_name(self):
#         enteredname=self.cleaned_data['name']
#         obj=Product.objects.get(name=enteredname).exists()
#         if obj:
#             raise ValidationError('name must be unique')
#         else:
#             return True

#-------------second way using Modelform
class productForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'#['name','image','price','category']

        
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
    