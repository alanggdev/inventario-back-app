# Generated by Django 4.1.7 on 2023-03-12 04:44

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_inventory', max_length=40)),
                ('products_name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('products', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('admins', models.ManyToManyField(related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', related_query_name='owner', to=settings.AUTH_USER_MODEL)),
                ('sellers', models.ManyToManyField(related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
