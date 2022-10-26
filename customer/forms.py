from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LogInForm(forms.Form):
    username=forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={"class":"form-label","placeholder":"Username"}))
    password=forms.CharField(label_suffix=' ',label=" ",widget=forms.PasswordInput(attrs={"class":"form-label","placeholder":"Password"}))

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label=" ",label_suffix=" ",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    password2 = forms.CharField(label=" ",label_suffix=" ",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":" Confirm Password"}))
    first_name = forms.CharField(label=" ", label_suffix=" ",
                                 widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}))
    last_name = forms.CharField(label=" ", label_suffix=" ",
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}))
    email = forms.CharField(label=" ",label_suffix=" ",widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}))
    username = forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]


class  CartsForm(forms.Form):
    qty=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class OrderForm(forms.Form):
    delivery_address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))



