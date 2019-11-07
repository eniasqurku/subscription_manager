from django.urls import path, include

from service.views import ServiceListView, ServiceDeleteView

service_urls = (
    [
        path('list', ServiceListView.as_view(), name='list'),
        path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete')
    ], 'service')

urlpatterns = [
    path('service/', include(service_urls))
]
