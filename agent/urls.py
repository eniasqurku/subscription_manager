from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import CustomerCreateListView, CustomerUpdateDeleteView

customer_urls = (
    [
        path('', CustomerCreateListView.as_view(), name='create_list'),
        path('<int:pk>/', CustomerUpdateDeleteView.as_view(), name='detail')

    ], 'customer')

urlpatterns = [
    path('customer/', include(customer_urls))
]
