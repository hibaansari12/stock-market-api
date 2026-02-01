from rest_framework.views import APIView
from rest_framework.response import Response
from stocks.models import StockData
from stocks.serializers import StockSerializer

class StockListAPIView(APIView):
    def get(self, request):
        stocks = StockData.objects.all()[:50]
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


class StockDetailAPIView(APIView):
    def get(self, request, symbol):
        stocks = StockData.objects.filter(company__symbol=symbol)
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
