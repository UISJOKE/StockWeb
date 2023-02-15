from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import StockView
from . import views


urlpatterns = [
    path('', views.mainOfStock, name='Main-of-Stock'),
   # path('search', views.post_search, name='stock-search'),
    path('add', views.addToStock, name='add-to-stock'),
    path('stock', login_required(StockView.as_view(template_name='index.html')),name='stock-home'),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
