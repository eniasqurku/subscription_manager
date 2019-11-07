from django.db import models


# Create your models here.
class Customer(models.Model):
    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klientët'
        db_table = 'customer'

    name = models.CharField(max_length=50)
    nuis = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
