# Generated by Django 3.1.7 on 2021-03-06 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rich', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rich.category'),
        ),
        migrations.AddField(
            model_name='asset',
            name='written_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]