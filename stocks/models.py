from django.db import models

# Create your models here.

class Company(models.Model):
    SYMBOL_CHOICES = [
        ("AAPL", "Apple Inc (AAPL)"),
        ("MSFT", "Microsoft (MSFT)"),
        ("GOOG", "Google (GOOG)"),
        ("TSLA", "Tesla (TSLA)"),
        ("AMZN", "Amazon (AMZN)"),
    ]
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, choices=SYMBOL_CHOICES, unique=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class StockData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    daily_return = models.FloatField(null=True, blank=True)
    ma7 = models.FloatField(null=True, blank=True)
    week_52_high = models.FloatField(null=True, blank=True)
    week_52_low = models.FloatField(null=True, blank=True)
    volatility = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('company', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.company.symbol} - {self.date}"
