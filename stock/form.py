from django import forms


from django import forms
from django.forms import Textarea
from .models import Stock

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ["article", "name","photo", "description", "country", "net_weight", "gross_weight", "price"]

        widgets = {
            'description': Textarea(attrs={'class': 'my-litte-class'}),
        }
