# Generated by Django 3.0.1 on 2020-01-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200110_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderadress',
            name='phone',
            field=models.IntegerField(default=1),
        ),
    ]
