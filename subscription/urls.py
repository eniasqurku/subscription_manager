from django.urls import path, include

from subscription.views import SubscriptionCreateListView, SubscriptionUpdateDeleteView

subscription_urls = (
    [
        path('', SubscriptionCreateListView.as_view(), name='create_list'),
        path('<int:pk>/', SubscriptionUpdateDeleteView.as_view(), name='detail')
    ], 'subscription')

urlpatterns = [
    path('subscription/', include(subscription_urls))
]
