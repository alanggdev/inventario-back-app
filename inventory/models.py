from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class InventoryModel(models.Model):
    name = models.CharField(max_length=40, null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='owner', related_query_name='owner')
    admins = models.ManyToManyField(User, related_name='admin', blank=True)
    sellers = models.ManyToManyField(User, related_name='seller', blank=True)
    products_name = ArrayField(models.CharField(max_length=30, null=True), null=True)
    products = ArrayField(models.IntegerField(null=True), null=True)