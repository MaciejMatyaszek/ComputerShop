# Generated by Django 3.0.1 on 2020-01-10 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20200110_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderadress',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Order'),
        ),
    ]
