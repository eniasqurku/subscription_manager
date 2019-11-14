from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Customer
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status


class CustomerCreateListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def delete(self, request, *args, **kwargs):
        customer = self.get_object()
        if customer.subscriptions.all():
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
