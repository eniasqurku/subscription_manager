"""subscription_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path

import agent.urls as customer_urls
import service.urls as service_urls
import subscription.urls as subscription_urls
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='agent/login.html'), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', logout_then_login, name='logout'),

]

urlpatterns += service_urls.urlpatterns
urlpatterns += subscription_urls.urlpatterns
urlpatterns += customer_urls.urlpatterns
