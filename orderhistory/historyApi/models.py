from django.db import models


# Create your models here.

class Order(models.Model):
    bid_sell = models.CharField(max_length=20)
    purchase_sell_date = models.DateField()
    bitcoin_amount = models.FloatField()
    actual_amount = models.FloatField()

    def __str__(self):
        return f'{self.bid_sell}, {self.actual_amount}, {self.bitcoin_amount}'
