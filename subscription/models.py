from django.db import models
from agent.models import Customer
from service.models import Service
from django.forms import Widget,SelectDateWidget


# Create your models here.
class Subscription(models.Model):
    class Meta:
        verbose_name='abonimi'
        verbose_name_plural='abonimet'
        db_table='Subscription'


    start_date = models.DateField('Data e fillimit')
    end_date = models.DateField('Data e mbarimit')
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, related_name='subscriptions', on_delete=models.DO_NOTHING, null=True)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.DO_NOTHING)
