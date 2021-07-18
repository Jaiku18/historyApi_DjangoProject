from historyApi.models import Order
from rest_framework import generics
from historyApi.api.serializer import OrderSerializers
from historyApi.api.pagenation import smallPagination
from django.views.generic import View
from django.shortcuts import render


class BaseView(generics.ListAPIView):
    pagination_class = smallPagination
    serializer_class = OrderSerializers


class BitHistory(BaseView):
    queryset = Order.objects.all()
    filter_fields = {'bid_sell': ['exact'], 'purchase_sell_date': ['gte', 'lte'], 'bitcoin_amount': ['gte', 'lte'],
                     'actual_amount': ['gte', 'lte']}


class BitHistorySearch(BaseView):
    queryset = Order.objects.all()
    filter_fields = {'bid_sell': ['exact'], 'purchase_sell_date': ['exact'], 'bitcoin_amount': ['exact'],
                     'actual_amount': ['exact']}


class HomeView(View):
    def get(self, request):
        return render(request, 'Home.html')


"""
######################OTHER TRIED METHODS##################
class Order_list_generic_class(generics.ListAPIView):
    pagination_class = smallPagination
    queryset = Order.objects.filter(name__gte=100, name__lte=123)
    serializer_class = OrderSerializers
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['bid_sell', 'purchase_sell_date','bitcoin_amount','actual_amount']
    filter_backends = SearchFilter
    search_fields = ['bid_sell', 'purchase_sell_date','bitcoin_amount','actual_amount']

    filter_fields = ('bid_sell', 'purchase_sell_date', 'bitcoin_amount', 'actual_amount',)

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)
    def get_queryset(self):
        queryset = Order.objects.all()
        query = self.request.query_params.get("q", None)
        purchase = self.request.query_params.get("purchase_sell_date", None)
        bitcoin_amount = self.request.query_params.get("bitcoin_amount", None)
        actual_amount = self.request.query_params.get("actual_amount", None)
        filter_fields = (
            'robot_category',
            'manufacturer',
        )
        if query:
            queryset = queryset.filter(Q(bid_sell=query)|
                                       Q(bitcoin_amount=query)|
                                       Q(actual_amount=query))
        return queryset


    def get_queryset(self, *args,**kwargs):
        queryset = Order.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(Q(bid_sell=query)|
                                       Q(purchase_sell_date=query) |
                                       Q(bitcoin_amount=query)|
                                       Q(actual_amount=query))
        return queryset
        
    class OrderSearchFilter(BaseView):
    filter_fields = ('bid_sell', 'purchase_sell_date', 'bitcoin_amount', 'actual_amount',)
    #filter_fields = {'bid_sell':['gte', 'lte'], 'purchase_sell_date':['gte', 'lte'], 'bitcoin_amount': ['gte', 'lte'], 'actual_amount':['gte', 'lte']}

    class OrderFilter(BaseView):
    
        def get_queryset(self):
            search_filter_fields = dict(self.request.GET)
            for key in search_filter_fields.keys():
                search_filter_fields[key] = search_filter_fields[key][0]
            print(search_filter_fields)
            print()
            print(self.get_paginated_response(Order.objects.filter(**search_filter_fields)))
            return Order.objects.filter(**search_filter_fields)
"""
