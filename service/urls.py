from django.urls import path, include
from django.contrib.auth.decorators import login_required
from service.views import ServiceListView, ServiceDeleteView, ServiceCreateView, ServiceUpdateView

service_urls = (
    [
        path('', login_required(ServiceListView.as_view()), name='list'),
        path('delete/<int:pk>/', login_required(ServiceDeleteView.as_view()), name='delete'),
        path('create', login_required(ServiceCreateView.as_view()), name='create'),
        path('update/<int:pk>/', login_required(ServiceUpdateView.as_view()), name='update')
    ], 'service')

urlpatterns = [
    path('service/', include(service_urls))
]
