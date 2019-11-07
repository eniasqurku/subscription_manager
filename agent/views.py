from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Customer
from .forms import CustomerForm
from django.http import HttpResponseRedirect


# Create your views here.

class CustomerListView(ListView):
    template_name = 'customer/customer_list.html'
    queryset = Customer.objects.all()


class CustomerDeleteView(DeleteView):
    success_url = reverse_lazy('customer:list')
    model = Customer

    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        if customer.subscriptions.all():
            return HttpResponseRedirect(self.success_url)
        else:
            customer.delete()
            return HttpResponseRedirect(self.success_url)


class CustomerUpdateView(UpdateView):
    success_url = reverse_lazy('customer:list')
    form_class = CustomerForm
    queryset = Customer.objects.all()
    template_name = 'customer/update.html'


class CustomerCreateView(CreateView):
    success_url = reverse_lazy('customer:list')
    form_class = CustomerForm
    queryset = Customer.objects.all()
    template_name = 'customer/create.html'
