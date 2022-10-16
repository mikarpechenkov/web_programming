from django.shortcuts import render

from stock.models import Goods


def main_stock_page(request):
    goods = Goods.objects.all()
    return render(request, 'stock/stock.html', {'goods': goods})
