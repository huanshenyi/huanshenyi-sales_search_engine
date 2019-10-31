from django.db import models


class CrawlerData(models.Model):
    """
    クローラーデータ
    """
    company_name = models.CharField(max_length=30, null=False, default="", help_text="会社名", verbose_name="会社名")
    job_name = models.CharField(max_length=100, null=False, default="", help_text="仕事内容", verbose_name="仕事内容")
    link_url = models.CharField(max_length=150, null=False, default="", help_text="詳細リンク", verbose_name="詳細リンク")
    nearest_station = models.CharField(max_length=50, null=True, default="", help_text="住所", verbose_name="住所")
    longitude = models.CharField(max_length=20, null=True, default="", help_text="経度", verbose_name="経度")
    latitude = models.CharField(max_length=20, null=True, default="", help_text="緯度", verbose_name="緯度")
    source = models.CharField(max_length=20, null=False, help_text="出所", verbose_name="出所")
    occupation = models.CharField(max_length=50, null=False, default="", help_text="職種", verbose_name="職種")
    annual_income_min = models.IntegerField(null=True, default=0, help_text="最低提示年収", verbose_name="最低提示年収")
    annual_income_max = models.IntegerField(null=True, default=0, help_text="最高提示年収", verbose_name="最高提示年収")
    published_time = models.CharField(max_length=100, null=True, default="", help_text="サイト内での掲載時間", verbose_name="サイト内での掲載時間")
    create_data = models.CharField(max_length=30, null=False, help_text="スクロール時間", verbose_name="スクロール時間")

    class Meta:
        verbose_name = "クローラデータ"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_name

