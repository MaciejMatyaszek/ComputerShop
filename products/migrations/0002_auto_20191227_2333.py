# Generated by Django 3.0.1 on 2019-12-27 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa Kategorii')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Odnośnik')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Klient', 'verbose_name_plural': 'Klienci'},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='products.Category', verbose_name='Kategorie'),
        ),
    ]
