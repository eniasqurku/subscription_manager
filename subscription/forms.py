from django.forms import ModelForm, Widget, SelectDateWidget
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
            'start_date': SelectDateWidget(),
            'end_date' : SelectDateWidget()
        }
