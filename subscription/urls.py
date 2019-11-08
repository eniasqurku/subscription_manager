from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login
from subscription.views import SubscriptionListView, SubscriptionDeleteView, SubscriptionCreateView, SubscriptionUpdateView
from django.contrib.auth.decorators import login_required

subscription_urls = (
    [
        path('', login_required(SubscriptionListView.as_view()), name='list'),
        path('delete/<int:pk>/', login_required(SubscriptionDeleteView.as_view()), name='delete'),
        path('create', login_required(SubscriptionCreateView.as_view()), name='create'),
        path('update/<int:pk>/', login_required(SubscriptionUpdateView.as_view()), name='update')
    ], 'subscription')

urlpatterns = [
    path('subscription/', include(subscription_urls))
]
