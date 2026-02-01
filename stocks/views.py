from django.shortcuts import render

# Create your views here.

# stocks/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StockData, Company
from .serializers import StockSerializer

class StockListAPIView(APIView):
    def get(self, request):
        qs = StockData.objects.all()
        serializer = StockSerializer(qs, many=True)
        return Response(serializer.data)

class StockDetailAPIView(APIView):
    def get(self, request, symbol):
        try:
            company = Company.objects.get(symbol=symbol)
            qs = StockData.objects.filter(company=company)
            serializer = StockSerializer(qs, many=True)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)
