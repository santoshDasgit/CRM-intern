from django import forms
from .models import User


# senior teacher can create the user form
class userCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password','user_type','is_active','is_admin']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control my-2'}),
            'last_name': forms.DateTimeInput(attrs={'class': 'form-control my-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control my-2'}),
            'user_type': forms.Select(attrs={'class': 'form-control my-2'}),
          
        }


# senior teacher can update the user info form
class userChangeFm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','user_type','is_active','is_admin']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control my-2'}),
            'last_name': forms.DateTimeInput(attrs={'class': 'form-control my-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'user_type': forms.Select(attrs={'class': 'form-control my-2'}),
          
        }