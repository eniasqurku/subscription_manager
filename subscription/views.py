from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Subscription
from .forms import SubscriptionForm
# Create your views here.

class SubscriptionListView(ListView):
    template_name = 'subscription/subscription_list.html'
    queryset = Subscription.objects.all()

class SubscriptionCreateView(CreateView):
    success_url = reverse_lazy('subscription:list')
    template_name = 'subscription/create.html'
    form_class = SubscriptionForm
    queryset = Subscription.objects.all()

class SubscriptionDeleteView(DeleteView):
    success_url = reverse_lazy('subscription:list')
    model = Subscription

class SubscriptionUpdateView(UpdateView):
    success_url = reverse_lazy('subscription:list')
    form_class = SubscriptionForm
    queryset = Subscription.objects.all()
    template_name = 'subscription/update.html'