# Generated by Django 3.1.7 on 2021-03-14 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rich', '0041_stocktrade_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='code_or_ticker',
        ),
    ]
