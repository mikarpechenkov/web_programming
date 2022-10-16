from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_stock_page, name='stock')
]