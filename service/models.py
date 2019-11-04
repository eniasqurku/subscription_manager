from django.db import models


# Create your models here.

class ServiceType(models.Model):
    name = models.CharField(max_length=20)


class Service(models.Model):
    name = models.CharField(max_length=50)
    service_type = models.ForeignKey(ServiceType, related_name='services', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
