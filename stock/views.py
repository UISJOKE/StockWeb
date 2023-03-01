from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Stock, Procurement, WriteOff, User,Buyer, Provider
from .form import StockForm, UserRegisterForm, WriteOffForm, ProcurementForm, BuyerForm


class WriteOffView(CreateView):
    model = WriteOff
    form_class = WriteOffForm
    template_name = 'stock/minus_item.html'
    success_url = reverse_lazy('stock-home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('login')

        return super().dispatch(request, *args, **kwargs)

class CreateBuyerView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'stock/add_buyer.html'
    success_url = reverse_lazy('writeoff')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('login')

        return super().dispatch(request, *args, **kwargs)


class CreateProcurementView(CreateView):
    model = Procurement
    form_class = ProcurementForm
    template_name = 'stock/plus_item.html'
    success_url = reverse_lazy('stock-home')


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('login')

        return super().dispatch(request, *args, **kwargs)


class StockView(ListView):
    model = Stock
    template_name = 'red.html'
    context_object_name = 'stock'

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        if ordering == 'По убыванию цены':
            ordering = '-price'
        elif ordering == 'По возрастанию цены':
            ordering = 'price'
        elif ordering == 'От старых к новым':
            ordering = 'id'
        else:
            ordering = '-id'
        return ordering



    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('login')

        return super().dispatch(request, *args, **kwargs)


class CreateStockView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/add_in_stock.html'
    success_url = reverse_lazy('stock-home')


    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return reverse_lazy('login')
    #
    #     return super().dispatch(request, *args, **kwargs)


class ItemProfile(DetailView):
    model = Stock
    template_name = 'stock/profile_item.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('login')

        return super().dispatch(request, *args, **kwargs)


class UserProfileView(DetailView):
    model = User
    template_name = 'registration/profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse_lazy('login')

        return super().dispatch(request, *args, **kwargs)

class StockUpdateView(UpdateView):
    model = Stock
    template_name = 'stock/edit_item.html'
    fields = ['article', 'name', 'photo', 'description', 'net_weight', 'gross_weight', 'price']
    success_url = reverse_lazy('stock-home')

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return reverse_lazy('login')
    #
    #     return super().dispatch(request, *args, **kwargs)


@login_required()
def mainOfStock(request):
    return redirect('stock-home')


def book_list(request):
    # sort_type = request.GET.get('type')
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


def checkbox_delete(request):
    if request.method == 'POST':
        items = request.POST.getlist('id')
        print(items)
        for item in items:
            Stock.objects.filter(id=item).delete()

        return HttpResponseRedirect("/")

    return render(request, 'red.html')

class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'red.html'
    success_url = reverse_lazy('stock-home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('stock-home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'reg': form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')
