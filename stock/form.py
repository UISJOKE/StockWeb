from django import forms
from django.forms import Textarea
from .models import Stock
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["article", "name", "photo", "description", "country",
                  "net_weight", "gross_weight", "price", "count"]

        widgets = {
            'description': Textarea(attrs={'class': 'my-litte-class'}),
        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']