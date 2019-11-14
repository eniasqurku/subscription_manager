from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import generics


class SubscriptionCreateListView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer




