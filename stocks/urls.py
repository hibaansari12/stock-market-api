from django.urls import path
from .views import StockListAPIView, StockDetailAPIView

urlpatterns = [
    path('stocks/', StockListAPIView.as_view(), name='stock-list'),
    path('stocks/<str:symbol>/', StockDetailAPIView.as_view(), name='stock-detail'),
]
