from django.db import models

class CurrencyChoice(models.Model):
    email = models.EmailField(primary_key=True)  # Email as primary key
    currency_pair = models.CharField(max_length=10)  # E.g., "EURUSD"
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    buy_or_sell = models.CharField(max_length=5, choices=[
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ])

    def __str__(self):
        return f"{self.email} - {self.currency_pair} ({self.buy_or_sell})"

