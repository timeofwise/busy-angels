# Generated by Django 3.1.7 on 2021-03-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rich', '0039_auto_20210309_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='deposit_krw',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='deposit_usd',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.DeleteModel(
            name='Exchange',
        ),
    ]
