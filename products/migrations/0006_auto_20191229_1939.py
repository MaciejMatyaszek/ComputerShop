# Generated by Django 3.0.1 on 2019-12-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20191229_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(upload_to='icons/', verbose_name='Ikona Produktu'),
        ),
    ]