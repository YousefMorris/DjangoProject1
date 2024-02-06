from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import authenticate
from ecommerceapp.models import *
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
# def Mylogin(request):
#     context={'form':authenticate()}
#     return render(request,'registration/login.html',context)

def Myprofile(request):
    return redirect(reverse('productlist'))

# def Mylogout(request):
#     context={'form':authenticate()}
#     return render(request,'registration/login.html')
class Registrationform(CreateView):
    model=User
    template_name='registration/register.html'
    form_class=UserCreationForm
    context_object_name='form'
    success_url=reverse_lazy('login.html')
