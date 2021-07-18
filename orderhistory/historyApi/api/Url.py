from django.urls import path
from historyApi.api.views import BitHistorySearch, HomeView, BitHistory

urlpatterns = [
    path('order/', BitHistory.as_view(), name='order list'),
    path('home/', HomeView.as_view(), name='Home'),
    path('order/search', BitHistorySearch.as_view(), name='search')

]
