from django.forms import ModelForm
from .models import Subscription


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = [
            'start_date',
            'end_date',
            'service',
            'customer'
        ]
