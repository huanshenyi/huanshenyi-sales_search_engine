import django_filters

from .models import CrawlerData


class CrawlerDataFilter(django_filters.rest_framework.FilterSet):
    """
    クローラーデータのフィルター
    """
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='icontains')

    class Meta:
        model = CrawlerData
        fields = ["company_name"]
