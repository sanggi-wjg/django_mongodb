from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Items
from .mongo_db import MongoDB


class StockItemList(LoginRequiredMixin, ListView):
    model = Items
    context_object_name = 'stock_items'
    template_name = 'stock/stock_item_list.html'
    extra_context = {
        'view_title': 'Stock List'
    }


class StockItemDetail(LoginRequiredMixin, ListView):
    template_name = 'stock/stock_item_detail.html'
    context_object_name = 'stock_items'

    def get_queryset(self):
        return get_object_or_404(Items, code = self.kwargs['code'])

    def get_context_data(self, **kwargs):
        mongo = MongoDB()

        return {
            'view_title'  : 'Stock Detail',
            'stock_item'  : self.get_queryset(),
            'finance_info': mongo.find_one('finance_info', { "stock_items_code": self.kwargs['code'] })
        }
