from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Items
from .mongo_db import MongoDB


class StockItemList(LoginRequiredMixin, ListView):
    model = Items
    paginate_by = 10
    template_name = 'stock/stock_item_list.html'
    context_object_name = 'stock_items'
    extra_context = {
        'view_title': 'Stock List'
    }


class StockItemDetail(LoginRequiredMixin, DetailView):
    template_name = 'stock/stock_item_detail.html'
    context_object_name = 'stock_item'

    def get_object(self, queryset = None):
        return get_object_or_404(Items, code = self.kwargs['code'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Stock Detail'
        context['finance_info'] = MongoDB().find_one('finance_info', { "stock_items_code": self.kwargs['code'] })

        return context
