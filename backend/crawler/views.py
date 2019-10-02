from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets

from .models import CrawlerData
from .serializer import CrawlerDataSerializer


class CrawlerDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CrawlerData.objects.all()
    serializer_class = CrawlerDataSerializer
