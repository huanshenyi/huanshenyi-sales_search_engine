from rest_framework import serializers
from .models import CrawlerData


class CrawlerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlerData
        fields = "__all__"

