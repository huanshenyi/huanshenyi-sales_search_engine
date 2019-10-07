from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle

from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import CrawlerData
from .serializer import CrawlerDataSerializer, CrawlerMapDataSerializer
from .filters import CrawlerDataFilter


class CrawlerDataPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 200


class CrawlerDataViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    検索データ用
    """
    throttle_classes = (AnonRateThrottle,)
    queryset = CrawlerData.objects.all()
    serializer_class = CrawlerDataSerializer
    pagination_class = CrawlerDataPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CrawlerDataFilter
    search_fields = ['company_name']


class CrawlerMapDataViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    マップデータ用
    """
    throttle_classes = (AnonRateThrottle, )
    queryset = CrawlerData.objects.all()
    serializer_class = CrawlerMapDataSerializer
    pagination_class = CrawlerDataPagination

