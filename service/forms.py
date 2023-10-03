from django.forms import ModelForm

from service.models import Service, ServiceType


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'service_type']


class ServiceTypeForm(ModelForm):
    class Meta:
        model = ServiceType
        fields = ['name']
