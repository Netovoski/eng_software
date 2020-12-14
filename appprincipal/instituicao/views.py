from appprincipal.instituicao.forms import *
from appprincipal.instituicao.models import *
from appprincipal.registration.models import *
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


class InstituicaoTemplateView(TemplateView):
    template_name = "instituicao/instacesso.html"
    @method_decorator(allowed_users(allowed_roles=['admin', 'coord', 'super', 'dirigente', 'diretor']))
    @method_decorator(login_required)
    def get (self, request):
        return render(request, self.template_name)


class Cadast_InstParCreateView(CreateView):
    template_name = "instituicao/cadast_instpar.html"
    model = Inst_Par
    fields = '__all__'
    success_url = reverse_lazy("instituicao:lista_instpar")
    @method_decorator(allowed_users(allowed_roles=['admin', 'dirigente', 'diretor']))
    @method_decorator(login_required)
    def get (self, request):

        return render(request, self.template_name)


class Update_InstParUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "instituicao/update_instpar.html"
    model = Inst_Par
    fields = '__all__'
    #fields = ['nome_instituicao']
    context_object_name = "inst_par"
    success_url = reverse_lazy("instituicao:lista_instpar")
    #@method_decorator(allowed_users(allowed_roles=['admin']))
    #@method_decorator(login_required)
    # def get (self, request, pk):

    #     return render(request, self.template_name)

class Cadast_InstValCreateView(CreateView):
    template_name = "instituicao/cadast_instval.html"
    model = Inst_Val
    form_class = RegistrarInst_ValForm
    success_url = reverse_lazy("instituicao:lista_instval")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'super']))
    def get (self, request):
        return render(request, self.template_name)

class Update_InstValUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "instituicao/update_instval.html"
    model = Inst_Val
    fields = '__all__'
    #fields = ['nome_instituicao']
    context_object_name = "inst_val"
    success_url = reverse_lazy("instituicao:lista_instval")


class Cadast_FuncionarioCreateView(CreateView):
    template_name = "instituicao/cadast_func.html"
    model = Usuario
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy("regis:usuarios")
    #@method_decorator(allowed_users(allowed_roles=['admin']))
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'super']))
    def get (self, request):

        return render(request, self.template_name)

class Cadast_DirigenteParCreateView(CreateView):
    template_name = "instituicao/cadast_dirigentepar.html"
    model = DirigentePar
    form_class = RegistrarDirigenteParForm
    success_url = reverse_lazy("appprincipal:index")
    #@method_decorator(allowed_users(allowed_roles=['admin']))
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin','diretor']))
    def get (self, request):

        return render(request, self.template_name)

class Cadast_DirigenteValCreateView(CreateView):
    template_name = "instituicao/cadast_dirigenteval.html"
    model = DirigenteVal
    form_class = RegistrarDirigenteValForm
    success_url = reverse_lazy("appprincipal:index")
    #@method_decorator(allowed_users(allowed_roles=['admin']))
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin','super']))
    def get (self, request):

        return render(request, self.template_name)

class Cadast_DiretorParCreateView(CreateView):
    template_name = "instituicao/cadast_diretorpar.html"
    model = DiretorPar
    form_class = RegistrarDiretorParForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'diretor']))
    def get (self, request):

        return render(request, self.template_name)

class Cadast_SuperValCreateView(CreateView):
    template_name = "instituicao/cadast_superval.html"
    model = SuperVal
    form_class = RegistrarSuperValForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'super']))
    def get (self, request):

        return render(request, self.template_name)

@login_required
def InstParListView(ListView):
    #funcionario
    instpar = Inst_Par.objects.all()
    
    contexto = {
        'instpar': instpar
    }
    
    return render(ListView, "instituicao/instpar.html",contexto)

@login_required
def InstValListView(ListView):
    #funcionario
    instval = Inst_Val.objects.all()
    
    contexto = {
        'instval': instval
    }
    
    return render(ListView, "instituicao/instval.html",contexto)


