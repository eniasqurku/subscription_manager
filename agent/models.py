from django.db import models


class Customer(models.Model):
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table = 'customer'

    name = models.CharField(max_length=50)
    nuis = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
