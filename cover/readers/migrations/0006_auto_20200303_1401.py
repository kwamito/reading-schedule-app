# Generated by Django 3.0.3 on 2020-03-03 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('readers', '0005_auto_20200303_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
