from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Service, ServiceType
from django.views import generic


# Create your views here.

# def shfaq_sherbimet(request):
#   sherbimet=Service.objects.all()
#  return render(request,"service_list.html",{})

# class sherbimet(generic.ListView):
#    template_name = 'service_list.html'
#   context_object_name = 'sherb'

#    def get_queryset(self):
#       return Service.objects.order_by('service_type_id')[:5]

def sherbimet(request):
    context = {
        "services": Service.objects.all()
    }
    return render(request, 'service/service_list.html', context)


def delete(request, name):
    obj = get_object_or_404(Service, name=name)
    obj.delete()
    context = {
        "services": Service.objects.all()
    }
    return render(request, 'service/service_list.html', context)


def form(request):
    context = {

    }
    return render(request, "service/create_service.html", context)


def add(request, ):
    Service.objects.create(name=request.POST['name'])
    return HttpResponseRedirect(reverse_lazy('services'))


def update(request, pk):
    obj = Service.objects.get(id=pk)

    pass
