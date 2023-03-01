from django import forms
from django.forms import Textarea
from .models import Stock,WriteOff,Procurement,User, Buyer, Provider
from django.contrib.auth.forms import UserCreationForm


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["article", "name", "photo", "description", "country",
                  "net_weight", "gross_weight", "price", "count", 'provider', 'user']

        widgets = {
            'description': Textarea(attrs={'class': 'my-litte-class'}),
        }

class WriteOffForm(forms.ModelForm):
    class Meta:
        model = WriteOff
        fields = ["article", "date", "action", "contact", "count",
                  "user"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = ['item', 'provider', 'count', 'price', 'datetime', 'user']


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['ESSENCE', 'contact', 'adress', 'contact_number', 'Requisites']
