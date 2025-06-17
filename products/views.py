from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]   # <- both filters
    search_fields = ['name']                                # <- must be INSIDE class
    filterset_fields = ['category']
    pagination_class = ProductPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # 💰 Price range filters
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset
