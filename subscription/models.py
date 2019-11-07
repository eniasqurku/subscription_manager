from django.db import models
from agent.models import Customer
from service.models import Service
# Create your models here.
class Subscription(models.Model):
    start_date = models.DateField("Date")
    end_date = models.DateField("Date")
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING, null=True)
    service = models.ForeignKey()
