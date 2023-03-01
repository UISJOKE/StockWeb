from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import StockView, ItemProfile, StockUpdateView, CreateStockView, StockDeleteView,\
    WriteOffView, CreateProcurementView, UserProfileView,CreateBuyerView
from . import views

urlpatterns = [
                  path('', views.mainOfStock, name='Main-of-Stock'),
                  path('stock', StockView.as_view(template_name='red.html'), name='stock-home'),
                  path('', include('django.contrib.auth.urls')),
                  path("create", CreateStockView.as_view(), name='create_stock'),
                  path('search', views.search, name='search'),
                  path('list', views.book_list, name='list'),
                  path('delete/<int:pk>', StockDeleteView.as_view(), name='del'),
                  path('delete/', views.checkbox_delete, name='checkdel'),
                  path('register/', views.register, name='register'),
                  path('profile/<int:pk>', UserProfileView.as_view() , name='profile'),
                  path('item/<int:pk>', ItemProfile.as_view(), name='item'),
                  path('edit/<int:pk>', StockUpdateView.as_view(), name='edit_item'),
                  path('writeoff', WriteOffView.as_view(), name='writeoff'),
                  path('proc', CreateProcurementView.as_view(), name='proc'),
                  path('nbuyer', CreateBuyerView.as_view(), name='buyer')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
