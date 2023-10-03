from django.forms import ModelForm, DateInput

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
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'})
        }
