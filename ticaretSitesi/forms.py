
from django import forms
from django.forms import TextInput,Textarea
from .models import Customer


class CustormerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')
        labels = {
            'title':"Culto Name",
            'description':"Culto Description",
            'date':"Movie date: dd-mm-yyyy",
            'slug':"Slug: peliculas-de-culto",
            'isActive':"Want to publish?",
            'isHome':"Want to see Home Page?"
            
        }
        widgets = {
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "date":TextInput(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
        }