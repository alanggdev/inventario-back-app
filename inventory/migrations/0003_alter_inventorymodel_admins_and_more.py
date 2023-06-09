# Generated by Django 4.1.7 on 2023-03-12 04:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_alter_inventorymodel_admins_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='sellers',
            field=models.ManyToManyField(blank=True, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
