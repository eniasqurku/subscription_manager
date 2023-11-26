from django.db import models


class ServiceType(models.Model):
    class Meta:
        verbose_name = 'Service Type'
        verbose_name_plural = 'Service Types'
        db_table = 'service_type'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Service(models.Model):
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        db_table = 'service'

    name = models.CharField(max_length=50)
    service_type = models.ForeignKey(ServiceType, related_name='services', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
