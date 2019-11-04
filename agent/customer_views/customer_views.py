from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from agent.models import Customer


class CustomerListView(ListView):
    model = Customer
    queryset = Customer.objects.all()
    template_name = 'customer_list.html'
    context_object_name = 'customers'
