from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'name',
                'placeholder': 'Username',
                'aria-describedby': 'basic-addon1'
            }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
                'type': 'password',
                'placeholder': 'Password',
                'for': 'form3Example4c'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
                'type': 'password',
                'placeholder': 'Password',
                'for': 'form3Example4c'
    }))


class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'name',
                'placeholder': 'Максат Мадаминов',
                'id': 'floatingInput',

            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
                'type': 'password',
                'placeholder': 'Пароль',
                'id': 'floatingPassword'
    }))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Shipment
        exclude = ['user', 'status']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'orderTitle'
            }),
            'origin': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'orderOrigin'
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'orderDestination'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'orderWeight',
                'type': 'number'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'orderPhone',
                'type': 'text',
                'value': '+996'
            }),
            'assigned_truck': forms.Select(attrs={
                'class': 'form-select',
                'id': 'orderTruck'
            }),
        }


class TruckForm(forms.ModelForm):

    
    class Meta:
        model = Truck
        exclude = ['driver',]

        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'id': 'truckImage',
            }),
            'plate_number': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'truckNumber',
                'placeholder': 'AC 972 D'
            }),
            'model': forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'truckModel',
            'placeholder': 'Volvo 23d-7'
            }),
            'capacity': forms.TextInput(attrs={
            'type': 'float',
            'class': 'form-control',
            'id': 'truckCapacity',
            'placeholder': '2452.521'
            })
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['license_front', 'license_back', 'phone_number', 'email', 'name']

        widgets = {
            'license_front': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'id': 'driverLicenseFront',
            }),
            'license_back': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'id': 'driverLicenseBack',
            }),
            'phone_number': forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'driverPhone',
            'value': '+996'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'driverName',
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': 'form-control',
                'id': 'driverEmail',
                'value': 'zoi@example.com'
            }),

        }