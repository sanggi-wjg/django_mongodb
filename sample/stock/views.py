from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Items


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
    extra_context = {
        'view_title': 'Stock Detail'
    }

    def get_queryset(self):
        # try :
        #     result = Items.objects.get(code = self.kwargs['code'])
        # except Items.DoesNotExist:
        #     raise Http404('Code does not exist')
        return get_object_or_404(Items, code = self.kwargs['code'])
