from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Stock


class StockView(ListView):
    model = Stock
    template_name = 'index.html'
    context_object_name = 'stock'

def mainOfStock(request):
    return render(request,'registration/login.html')


