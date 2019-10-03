from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import CrawlerData
from .serializer import CrawlerDataSerializer
from .filters import CrawlerDataFilter


class CrawlerDataPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 100


class CrawlerDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CrawlerData.objects.all()
    serializer_class = CrawlerDataSerializer
    pagination_class = CrawlerDataPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CrawlerDataFilter
    search_fields = ['company_name']

