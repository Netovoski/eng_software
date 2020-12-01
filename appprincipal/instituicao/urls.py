from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path


from appprincipal.instituicao.views import *

app_name = 'instituicao'

urlpatterns = [
    path('cria_instituicao/', InstituicaoCreateView.as_view(), name="cria_instituicao"),
    path('cria_dirigente/', DirigenteCreateView.as_view(), name="cria_dirigente"),

]