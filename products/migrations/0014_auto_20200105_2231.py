# Generated by Django 3.0.1 on 2020-01-05 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200105_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered_data',
            new_name='ordered_date',
        ),
    ]
