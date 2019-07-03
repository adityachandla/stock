from django.urls import path

from . import views

urlpatterns = [
	path('',views.Searcher.as_view(), name='search'),
	path('<str:symbol>/<str:name>', views.Stock.as_view(), name='stock_prices'),
]