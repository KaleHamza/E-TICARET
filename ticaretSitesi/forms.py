
from django import forms
from django.forms import TextInput
from .models import Customer, Product
from django.forms import ModelMultipleChoiceField, SelectMultiple, TextInput,Textarea

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
class CustormerSignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username','surname','password','email','password','phone','Current','adresses')
        labels = {
            'username':"username",
            'surname':"surname",
            'password':"password",
            'email':"e-mail",
            'password':"Password", 
            'phone':"phone",
            'Current':"Current",
            'adresses':"address",
            

        }
        widgets = {
            'username':TextInput(attrs={"class":"form-control"}),
            'surname':TextInput(attrs={"class":"form-control"}),
            'email':TextInput(attrs={"class":"form-control"}),
            "password":TextInput(attrs={"class":"form-control"}),
            'phone':TextInput(attrs={"class":"form-control"}),
            'Current':TextInput(attrs={"class":"form-control"}),
            'adresses':TextInput(attrs={"class":"form-control"}),
        }
class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields=('title','stock','slug',)
        labels = {
            'title':'title',
            'stock':"stock",
            
        }
        widgets = {
            'stock':TextInput(attrs={"class":"form-control"}),
            'title':TextInput(attrs={"class":"form-control"}),
           
            
        }
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model= Product
        fields=('__all__')
        labels = {
            'title':'title',
            'description':'description',
            'color':'color',
            'imageUrl':'imageUrl',
            'price':'price',
            'stock':"stock",
            'slug':"slug",
            'category':"category",
            
        }
        widgets = {
            
            'title':TextInput(attrs={"class":"form-control"}),
            'description':TextInput(attrs={"class":"form-control"}),
            'color':TextInput(attrs={"class":"form-control"}),
            'imageUrl':TextInput(attrs={"class":"form-control"}),
            'price':TextInput(attrs={"class":"form-control"}),
            'stock':TextInput(attrs={"class":"form-control"}),
            'slug':TextInput(attrs={"class":"form-control"}),
            "category": SelectMultiple(attrs={"class":"form-control"})
            
            
        }