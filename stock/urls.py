from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import StockView
from . import views


urlpatterns = [
    path('', views.mainOfStock, name='Main of Stock'),
    path('stock', StockView.as_view(template_name='index.html'), name='stock-home'),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)