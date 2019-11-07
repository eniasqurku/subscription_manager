from django.urls import path, include

from subscription.views import SubscriptionListView, SubscriptionDeleteView, SubscriptionCreateView, SubscriptionUpdateView

subscription_urls = (
    [
        path('', SubscriptionListView.as_view(), name='list'),
        path('delete/<int:pk>/', SubscriptionDeleteView.as_view(), name='delete'),
        path('create', SubscriptionCreateView.as_view(), name='create'),
        path('update/<int:pk>/', SubscriptionUpdateView.as_view(), name='update')
    ], 'subscription')

urlpatterns = [
    path('subscription/', include(subscription_urls))
]
