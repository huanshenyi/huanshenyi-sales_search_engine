from rest_framework import serializers
from .models import CrawlerData


class CrawlerDataSerializer(serializers.ModelSerializer):
    """
    検索のデータ一覧用
    """
    class Meta:
        model = CrawlerData
        fields = "__all__"


class CrawlerMapDataSerializer(serializers.ModelSerializer):
    """
    マップデータ用
    """
    class Meta:
        model = CrawlerData
        fields = ("company_name", "longitude", "latitude", "nearest_station", "annual_income_max")

