from appprincipal.instituicao.forms import *
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
# Create your views here.
from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.contrib.auth.decorators import login_required #para Functions Based Views
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
import requests

# class InstituicaoCreateView(CreateView):
#     template_name = "instituicao/cria_inst.html"
#     model = Instituicao
#     form_class = RegistrarUniversidadeCentralForm
#     success_url = "#"

#     def get(self, request):
#         return render(request, self.template_name)

# class DirigenteCreateView(CreateView):
#     template_name = "instituicao/cria_dirigente.html"
#     model = Dirigente
#     form_class = RegistrarDirigenteForm
#     success_url = "#"

#     def get(self, request):
#         return render(request, self.template_name)

class CriarInstituicaoParceiraCreateView(CreateView):
    #Dirigente

class AtualizarDadosInstituicaoParceiraUpdateView(UpdateView):
    #Diretor

class CriarInstValidadoraCreateView(CreateView):
    #Superintendente

class AtualizarDadosInstituicaoValidadoraUpdateView(UpdateView):
    #Superintendente

class ValidarInsituicaoParceira():
    #Superintendente valida (recebe/repassa) dados criados pelo dirigente 


