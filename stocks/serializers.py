from .models import StockData, Company
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="company.name",read_only=True)
    symbol = serializers.CharField(source="company.symbol",read_only=True)
    # company_name = serializers.CharField(
    #     source="company.name", read_only=True
    # )
    # symbol = serializers.CharField(
    #     source="company.symbol", read_only=True
    # )
    class Meta:
        model = StockData
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "symbol"]