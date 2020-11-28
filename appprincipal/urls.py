#from core.views import LocaisList, IndexTemplateView, LocalDetailView, RegCreateView, Pt1CreateView
from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path
from appprincipal.views import *
from . import views

app_name = 'appprincipal'

urlpatterns = [
    
    path('', IndexTemplateView.as_view(), name = 'index'),
]