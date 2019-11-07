from django.forms import Form, ModelForm

from agent.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['deleted']
