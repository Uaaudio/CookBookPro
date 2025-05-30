from django import forms
from django.contrib.auth.forms import UserCreationForm
from recipes.models import *




class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name', 'author_email', 'author_password']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'input'}),
            'author_email': forms.EmailInput(attrs={'class': 'input'}),
            'author_password': forms.PasswordInput(attrs={'class': 'input'}),
        }