from rest_framework import serializers
from historyApi.models import Order


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['id']
