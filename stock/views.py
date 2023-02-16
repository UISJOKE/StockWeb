from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .models import Stock
from .form import StockForm


class StockView(ListView):
    model = Stock
    template_name = 'index.html'
    context_object_name = 'stock'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('login/')

        return super().dispatch(request, *args, **kwargs)


class CreateStockView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/add_in_stock.html'
    success_url = reverse_lazy('stock-home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('login/')

        return super().dispatch(request, *args, **kwargs)


def mainOfStock(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        return redirect('stock-home')


def book_list(request):
    stock = Stock.objects.all()
    stock_dict = {'stock': stock}

    return render(request, stock_dict)


def search(request):

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':
            query = 'None'

        results = Stock.objects.filter(Q(name__icontains=query.capitalize()) |
                                       Q(article__icontains=query.capitalize()) |
                                       Q(name__icontains=query.casefold()) |
                                       Q(article__icontains=query.casefold()) |
                                       Q(country__icontains=query.casefold()) |
                                       Q(description__icontains=query.casefold()) |
                                       Q(country__icontains=query.capitalize()) |
                                       Q(description__icontains=query.capitalize()))


        return render(request, 'stock/search.html', {'query': query, 'results': results})
