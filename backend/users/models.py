from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    ユーザー
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="名前")
    mobile = models.CharField(null=True, blank=True, max_length=20, verbose_name="携帯番号")
    email = models.CharField(max_length=100, null=True, blank=True, unique=True, verbose_name="アドレス")

    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.username
