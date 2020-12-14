from django.shortcuts import render
from appprincipal.curso.forms import *
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
from appprincipal.curso.models import *
# Create your views here.

class CursoTemplateView(TemplateView):
    template_name = "curso/cursoacesso.html"
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['funcionario', 'coord', 'super', 'dirigente', 'diretor', 'admin']))
    def get (self, request):
        return render(request, self.template_name)

class Cadast_CursoCreateView(CreateView):
    #funcionario
    template_name = "curso/cadast_curso.html"
    model = Curso
    form_class = RegistrarTipoCursoForm
    success_url = reverse_lazy("curso:lista_curso")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['funcionario', 'super', 'diretor', 'admin']))
    def get (self, request):

        return render(request, self.template_name)

@login_required
def CursoListView(ListView):
    #funcionario
    cursos = Curso.objects.all()
    
    contexto = {
        'cursos': cursos
    }
    
    return render(ListView, "curso/cursos.html",contexto)


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    #funcionario
    template_name = "curso/atualiza_curso.html"
    model = Curso
    fields = '__all__'
    context_object_name = "curso"
    success_url = reverse_lazy("curso:lista_curso")
   #@method_decorator(allowed_users(allowed_roles=['funcionario', 'super', 'diretor', 'admin']))    
    # def get (self, request, pk):

    #     return render(request, self.template_name)

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "curso/exclui_curso.html"
    model = Curso
    context_object_name =  'curso'
    #@method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['funcionario', 'super', 'diretor', ]))
    def get_success_url (self):

        return reverse("curso:lista_curso")