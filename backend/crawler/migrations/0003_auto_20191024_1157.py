# Generated by Django 2.2.5 on 2019-10-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20191021_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawlerdata',
            name='annual_income_max',
            field=models.IntegerField(default=0, help_text='最高提示年収', null=True, verbose_name='最高提示年収'),
        ),
        migrations.AlterField(
            model_name='crawlerdata',
            name='annual_income_min',
            field=models.IntegerField(default=0, help_text='最低提示年収', null=True, verbose_name='最低提示年収'),
        ),
    ]