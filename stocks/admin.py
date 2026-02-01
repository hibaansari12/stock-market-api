from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ('name', 'symbol')

@admin.register(StockData)
class StockDataAdmin(admin.ModelAdmin):
    list_display = ('company', 'date', 'time', 'open_price', 'close', 'volume','low_price','high_price'
                    ,'daily_return','ma7','week_52_high','week_52_low','volatility')
    search_fields = ('company__name', 'company__symbol')
    list_filter = ('company', 'date')
    ordering = ('-date',)