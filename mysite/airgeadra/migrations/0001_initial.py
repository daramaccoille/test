# Generated by Django 5.0 on 2024-07-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyChoice',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('currency_pair', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buy_or_sell', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=5)),
            ],
        ),
    ]
