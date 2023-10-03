from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import ServiceForm
from .models import Service


class ServiceListView(LoginRequiredMixin, ListView):
    template_name = 'service/service_list1.html'
    context_object_name = 'services'
    queryset = Service.objects.all()


class ServiceCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('service:list')
    template_name = 'service/form.html'
    form_class = ServiceForm
    queryset = Service.objects.all()

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = reverse_lazy('service:create')
        return context"""


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('service:list')
    template_name = 'service/form.html'
    form_class = ServiceForm
    queryset = Service.objects.all()

    """def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Service, id=id_)"""

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['object1'] = ServiceType.objects.all()
        context['object'] = self.object
        return context"""


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('service:list')
    model = Service

    def delete(self, request, *args, **kwargs):
        service = self.get_object()
        if service.subscriptions.exists():
            return HttpResponseRedirect(self.success_url)
        else:
            service.delete()
            return HttpResponseRedirect(self.success_url)
