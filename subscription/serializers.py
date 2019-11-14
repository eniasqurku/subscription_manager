from .models import Subscription
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'start_date',
            'end_date',
            'customer',
            'service'
        ]
