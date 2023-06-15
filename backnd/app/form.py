from django import forms
from django.contrib.auth.models import User
from .models import user_type

# senior teacher can create the user form
class userCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name','first_name','password','username']
        widgets = {
          
            'last_name': forms.DateTimeInput(attrs={'class': 'form-control my-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control my-2'}),
            'username': forms.EmailInput(attrs={'class': 'form-control my-2'}),
          
        }
        labels = {
            'email':'',
            'username':'email'
        }


class User_type_creation_fm(forms.ModelForm):
    class Meta:
        model = user_type
        fields = ["type"]
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control my-2'}),
        }
          
        
          


# # senior teacher can update the user info form
class userChangeFm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name','first_name','username']
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control my-2'}),
            'last_name': forms.DateTimeInput(attrs={'class': 'form-control my-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2'}),
       
          
        }
        labels = {
            'email':'',
            'username':'email'
        }
