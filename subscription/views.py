from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import SubscriptionForm
from .models import Subscription


class SubscriptionListView(LoginRequiredMixin, ListView):
    template_name = 'subscription/list.html'
    queryset = Subscription.objects.all()


class SubscriptionCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('subscription:list')
    template_name = 'subscription/form.html'
    form_class = SubscriptionForm
    queryset = Subscription.objects.all()


class SubscriptionDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('subscription:list')
    model = Subscription


class SubscriptionUpdateView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('subscription:list')
    form_class = SubscriptionForm
    queryset = Subscription.objects.all()
    template_name = 'subscription/form.html'
