from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Items


def index(request):
    return HttpResponse('Hello Django')


def detail(request, code):
    try:
        stock = Items.objects.get(code = code)
    except Items.DoesNotExist:
        raise Http404('Code does not exist')

    return render(
        request = request,
        template_name = 'stock/stock_detail.html',
        context = {
            'stock': stock
        },
    )
