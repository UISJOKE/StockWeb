from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Stock
from .form import SearchForm
#from haystack.query import SearchQuerySet
class StockView(ListView):
    model = Stock
    template_name = 'index.html'
    context_object_name = 'stock'

def mainOfStock(request):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')
    else:
        return redirect('stock-home')
@login_required
def addToStock(request):
    return render(request,'stock/add_in_stock.html')

# def post_search(request):
#     form = SearchForm()
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             cd = form.cleaned_data
#             results = SearchQuerySet().models(Stock).filter(content=cd['query']).load_all()
#             # count total results
#             total_results = results.count()
#     return render(request,
#                   'stock/search.html',
#                   {'form': form,
#                    'cd': cd,
#                    'results': results,
#                    'total_results': total_results})
