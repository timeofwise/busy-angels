# Generated by Django 3.1.7 on 2021-03-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rich', '0003_asset_title_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='title_photo',
            field=models.ImageField(default='img/blog/no_pic.jpg', null=True, upload_to='img/blog_rich'),
        ),
    ]