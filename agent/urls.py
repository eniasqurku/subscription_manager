from django.urls import path, include

from agent.customer_views.customer_views import CustomerListView

customer_urls = (
    [
        path('list', CustomerListView.as_view(), name='list'),

    ], 'customer')
