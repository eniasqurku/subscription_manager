from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Service, ServiceType
from .serializers import ServiceSerializer
from rest_framework import generics


class ServiceCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def delete(self, request, *args, **kwargs):
        service = self.get_object()
        if service.subscriptions.all():
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
