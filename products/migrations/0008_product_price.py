# Generated by Django 3.0.1 on 2020-01-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191229_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Cena'),
            preserve_default=False,
        ),
    ]
