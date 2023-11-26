from django.urls import path, include

from .views import ServiceUpdateDeleteView, ServiceCreateListView

service_urls = (
    [
        path('', ServiceCreateListView.as_view(), name='create_list'),
        path('<int:pk>/', ServiceUpdateDeleteView.as_view(), name='detail')
    ], 'service')

urlpatterns = [
    path('service/', include(service_urls))
]
