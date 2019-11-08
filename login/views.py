from django.contrib.auth.views import LoginView
from django.http import request, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
