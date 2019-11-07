from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .models import Service, ServiceType
from .forms import ServiceForm

# Create your views here.

# def shfaq_sherbimet(request):
#   sherbimet=Service.objects.all()
#  return render(request,"service_list.html",{})

# class sherbimet(generic.ListView):
#    template_name = 'service_list.html'
#   context_object_name = 'sherb'

#    def get_queryset(self):
#       return Service.objects.order_by('service_type_id')[:5]

# def services(request):
#   context = {
#       "services": Service.objects.all()
#  }
# return render(request, 'service/service_list.html', context)


# def delete(request, pk):
#   obj = get_object_or_404(Service, id=pk)
#  obj.delete()
# # obj.save()
# context = {
#   "services": Service.objects.all()
# }
# return render(request, 'service/service_list.html', context)


"""def addform(request):
    obj = ServiceType.objects.all()
    context = {
        "object": obj
    }
    return render(request, "service/create_form.html", context)


def updateform(request, pk):
    obj = Service.objects.get(id=pk)
    obj1 = ServiceType.objects.all()
    context = {
        "object": obj,
        "object1": obj1
    }
    return render(request, "service/update_form.html", context)"""

"""def add(request):
    # obj = Service.objects.create(name=request.POST['name'],service_type=ServiceType.objects.get(name=request.POST['service_type']))
    obj = Service.objects.create(name=request.POST['name'], service_type_id=request.POST['service_type'])

    obj.save()
    return HttpResponseRedirect(reverse_lazy('services'))"""

"""def update(request, pk):
    obj = Service.objects.get(id=pk)
    obj.name = request.POST['name']
    obj.service_type_id = request.POST['service_type']
    obj.save()

    return HttpResponseRedirect(reverse_lazy('services'))"""


class ServiceListView(ListView):
    template_name = 'service/service_list.html'
    context_object_name = 'services'
    queryset = Service.objects.all()


class ServiceCreateView(CreateView):
    success_url = reverse_lazy('service:list')
    template_name = 'service/create_form1.html'
    form_class = ServiceForm
    queryset = Service.objects.all()

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = reverse_lazy('service:create')
        return context"""


class ServiceUpdateView(UpdateView):
    success_url = reverse_lazy('service:list')
    template_name = 'service/update_form1.html'
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


class ServiceDeleteView(DeleteView):
    success_url = reverse_lazy('service:list')
    model = Service

    def delete(self, request, *args, **kwargs):
        service = self.get_object()
        if service.subscriptions.all():
           return HttpResponseRedirect(self.success_url)
        else:
            service.delete()
            return HttpResponseRedirect(self.success_url)
