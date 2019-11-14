from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login
from subscription.views import SubscriptionCreateListView, SubscriptionUpdateDeleteView
from django.contrib.auth.decorators import login_required

subscription_urls = (
    [
        path('', SubscriptionCreateListView.as_view(), name='create_list'),
        path('<int:pk>/', SubscriptionUpdateDeleteView.as_view(), name='detail')
    ], 'subscription')

urlpatterns = [
    path('subscription/', include(subscription_urls))
]
