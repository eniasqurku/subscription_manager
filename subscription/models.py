from django.db import models

# Create your models here.
class Subscription(models.Model):
    start_date=models.DateTimeField
    end_date=models.DateTimeField
    date_created=models.DateTimeField(auto_now_add=True)
    date_last_updated=models.DateTimeField(auto_now=True)