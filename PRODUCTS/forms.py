from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#-----------------------------------------------------------------------------------------------------------------------

class RegisterUserForm(UserCreationForm):
    error_messages = {
        'Error.'
    }
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#-----------------------------------------------------------------------------------------------------------------------

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

#-----------------------------------------------------------------------------------------------------------------------

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

#-----------------------------------------------------------------------------------------------------------------------

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['account', 'fullname', 'email', 'address', 'city', 'state', 'code']

#-----------------------------------------------------------------------------------------------------------------------

class FavouriteForm(forms.ModelForm):
    class Meta:
        model = Favourite
        fields = '__all__'
        widgets = {
            'bond': forms.Select(attrs={'class': 'form-control'}),
            'film': forms.Select(attrs={'class': 'form-control'})
        }

#-----------------------------------------------------------------------------------------------------------------------

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'