# Generated by Django 3.0.1 on 2019-12-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191229_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Ikona Produktu'),
        ),
    ]
