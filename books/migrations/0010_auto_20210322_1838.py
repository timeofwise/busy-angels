# Generated by Django 3.1.7 on 2021-03-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210321_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='scrap',
            name='liked',
            field=models.IntegerField(default=0, null=True),
        ),
    ]