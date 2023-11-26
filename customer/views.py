from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import CustomerForm
from .models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    template_name = 'customer/list.html'
    queryset = Customer.objects.all()


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('customer:list')
    model = Customer

    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        if customer.subscriptions.all():
            return HttpResponseRedirect(self.success_url)
        else:
            customer.delete()
            return HttpResponseRedirect(self.success_url)


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('customer:list')
    form_class = CustomerForm
    queryset = Customer.objects.all()
    template_name = 'customer/form.html'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('customer:list')
    form_class = CustomerForm
    queryset = Customer.objects.all()
    template_name = 'customer/form.html'
