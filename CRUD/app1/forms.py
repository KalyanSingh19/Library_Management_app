from django.core import validators
from django import forms
from .models import Books

class BookRegistration(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['reg', 'title', 'issued', 'author', 'availability']
        widgets = {
            'reg': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'issued': forms.DateInput(attrs={'class':'my_date','placeholder':'YYYY-MM-DD'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            
        }

