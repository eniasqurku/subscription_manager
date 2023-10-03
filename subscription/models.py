from django.db import models

from agent.models import Customer
from service.models import Service


class Subscription(models.Model):
    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscription'
        db_table = 'subscription'

    start_date = models.DateField()
    end_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, related_name='subscriptions', on_delete=models.PROTECT, null=True)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
