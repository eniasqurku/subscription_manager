from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer


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
