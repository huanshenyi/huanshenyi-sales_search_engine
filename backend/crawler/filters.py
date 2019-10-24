import django_filters

from .models import CrawlerData


class CrawlerDataFilter(django_filters.rest_framework.FilterSet):
    """
    クローラーデータのフィルター
    """

    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='icontains')
    source = django_filters.CharFilter(field_name="source", lookup_expr="icontains")
    annual_income_min = django_filters.NumberFilter(field_name="annual_income_max", help_text="最低年収順", lookup_expr="gte")
    annual_income_max = django_filters.NumberFilter(field_name="annual_income_max", help_text="最高年収順", lookup_expr="lte")


    class Meta:
        model = CrawlerData
        fields = ["company_name", "source", "annual_income_min", "annual_income_max"]
