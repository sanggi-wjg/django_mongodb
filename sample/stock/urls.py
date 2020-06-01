from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import StockItemList, StockItemDetail

urlpatterns = [
    path('', StockItemList.as_view()),
    path('<str:code>', StockItemDetail.as_view()),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
