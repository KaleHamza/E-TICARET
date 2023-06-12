
from django import forms
from django.forms import TextInput
from .models import Customer, Product


class CustormerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('email','password',)
        labels = {
            'email':"e-mail",
            'password':"Password", 
        }
        widgets = {
            'email':TextInput(attrs={"class":"form-control"}),
            "password":TextInput(attrs={"class":"form-control"})
        }
class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields=('title','stock','slug',)
        labels = {
            'title':'title',
            'stock':"e-mail",
            
        }
        widgets = {
            'stock':TextInput(attrs={"class":"form-control"}),
            'title':TextInput(attrs={"class":"form-control"}),
           
            
        }