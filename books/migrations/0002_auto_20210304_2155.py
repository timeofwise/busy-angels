# Generated by Django 3.1.7 on 2021-03-04 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='sub_category',
            new_name='category',
        ),
    ]
