from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import CustomerDeleteView, CustomerCreateView, CustomerListView, CustomerUpdateView

customer_urls = (
    [
        path('', login_required(CustomerListView.as_view()), name='list'),
        path('delete/<int:pk>', login_required(CustomerDeleteView.as_view()), name='delete'),
        path('update/<int:pk>', login_required(CustomerUpdateView.as_view()), name='update'),
        path('create/', login_required(CustomerCreateView.as_view()), name='create'),

    ], 'customer')

urlpatterns = [
    path('customer/', include(customer_urls))
]
