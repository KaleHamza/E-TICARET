
from django import forms
from django.forms import TextInput,Textarea
from .models import Customer


class CustormerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username','surname','password','email','Current','adresses')
        labels = {
            'username':"User name",
            'surname':"Surname",
            'password':"Password",
            'email':"e-mail",
            'phone':"phone",
            'Current':"Current:",
            'adresses':"adress:"
            
        }
        widgets = {
            "username":TextInput(attrs={"class":"form-control"}),
            "surname":TextInput(attrs={"class":"form-control"}),
            "password":TextInput(attrs={"class":"form-control"}),
            "Current":TextInput(attrs={"class":"form-control"}),
            'phone':TextInput(attrs={"class":"form-control"}),
            'adresses':TextInput(attrs={"class":"form-control"}),
            'email':TextInput(attrs={"class":"form-control"})
        }