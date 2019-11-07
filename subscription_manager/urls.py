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
from django.contrib.auth.views import LoginView
from django.urls import path
from service import views
import service.urls as service_urls
import subscription.urls as subscription_urls
import  agent.urls as customer_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', 'bas'),
    # path('', views.Services.as_view(), name="services"),
    # path('delete/<int:pk>/', views.Delete.as_view(), name="delete"),
    # path('add', views.add, name="add"),
    # path('addform/', views.addform, name="addform"),
    # path('updateform/<int:pk>', views.updateform, name="updateform"),
    # path('update/<int:pk>', views.update, name="update"),
    # path('login', LoginView.as_view(template_name='agent/login.html'))
]

urlpatterns += service_urls.urlpatterns
urlpatterns += subscription_urls.urlpatterns
urlpatterns += customer_urls.urlpatterns
