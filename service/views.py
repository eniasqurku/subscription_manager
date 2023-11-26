from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Service
from .serializers import ServiceSerializer


class ServiceCreateListView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def delete(self, request, *args, **kwargs):
        service = self.get_object()
        if service.subscriptions.all():
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
