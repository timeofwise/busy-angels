# Generated by Django 3.1.7 on 2021-03-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rich', '0032_auto_20210308_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocktrade',
            name='io',
            field=models.IntegerField(null=True),
        ),
    ]
