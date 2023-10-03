from django.contrib.auth.decorators import login_required
from django.urls import path, include

from service.views import ServiceListView, ServiceDeleteView, ServiceCreateView, ServiceUpdateView

service_urls = (
    [
        path('', ServiceListView.as_view(), name='list'),
        path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete'),
        path('create', ServiceCreateView.as_view(), name='create'),
        path('update/<int:pk>/', ServiceUpdateView.as_view(), name='update')
    ], 'service')

urlpatterns = [
    path('service/', include(service_urls))
]
