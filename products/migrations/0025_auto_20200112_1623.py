# Generated by Django 3.0.1 on 2020-01-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20200111_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='promotion',
            field=models.BooleanField(default=False),
        ),
    ]
