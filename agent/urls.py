from django.urls import path, include

from .views import CustomerDeleteView, CustomerCreateView, CustomerListView, CustomerUpdateView

customer_urls = (
    [
        path('', CustomerListView.as_view(), name='list'),
        path('delete/<int:pk>', CustomerDeleteView.as_view(), name='delete'),
        path('update/<int:pk>', CustomerUpdateView.as_view(), name='update'),
        path('create/', CustomerCreateView.as_view(), name='create'),

    ], 'customer')

urlpatterns = [
    path('customer/', include(customer_urls))
]
