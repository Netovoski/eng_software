from django.shortcuts import render
from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse
from appprincipal.registration.models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views
from django.contrib.auth.forms import UserCreationForm #formulario Users
from django.contrib.auth.models import Group, User
from django.utils.decorators import method_decorator

from appprincipal.registration.forms import *
from django.views.generic.edit import UpdateView 
from django.contrib import messages
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
import json
import datetime

from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse

from appprincipal.registration.models import *


class RegistrationTemplateView(TemplateView):
    template_name = "registration/register.html"
    @method_decorator(allowed_users(allowed_roles=['admin', 'coord', 'super','dirigente', 'diretor']))
    @method_decorator(login_required)
    def get (self, request):
        return render(request, self.template_name)

class UsuariosCriarTemplateView(TemplateView):
    template_name = "registration/cria_users.html"
    @method_decorator(allowed_users(allowed_roles=['admin', 'super', 'diretor']))
    @method_decorator(login_required)
    def get (self, request):
        return render(request, self.template_name)



class UsuariosCriarSuperTemplateView(TemplateView):
    template_name = "registration/cria_userssuper.html"
	
	
@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, "Cadastro realizado com sucesso!"+ username)

			return redirect('appprincipal:index')
			

	context = {'form':form}
	return render(request, 'registration/registrar.html', context)


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect("appprincipal:index")
		else:
			messages.info(request, "Usuario ou senha incorreta")

	context = {}
	return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect("registration:login")

class UsuarioDeleteView(DeleteView):
    template_name = "registration/exclui_usuario.html"
    model = User
    context_object_name =  'usuario'
    #success_url = reverse_lazy("appprincipal:lista_produto")
    # @method_decorator(login_required)
    # @method_decorator(allowed_users(allowed_roles=['admin', 'super']))
    def get_success_url (self):
        return reverse('registration:usuarios')


@login_required
def UsersListView(request):
    usuario = User.objects.all()
    return render(request,"registration/usuarios.html", {"Usuario" : usuario})

def profileUpdate(request):
	usuario = User.objects.all()
	if request.method == 'POST':
		updateprofile = UserUpdateForm(request.POST, instance=request.user)
		if updateprofile.is_valid():
			updateprofile.save()
			messages.success(request, "Update realizado com sucesso!")
			return redirect('appprincipal:index')
	else:
		updateprofile = UserUpdateForm(instance=request.user)

		context ={
			'usuario': usuario,
			'updateprofile':updateprofile,
	}
	return render(request, 'registration/profile.html', context)

class UsersUpdateView(UpdateView):
    template_name = "registration/atualiza_user.html"
    model = User
    fields = ['username', 'email']
    context_object_name = "usuario"
    success_url = reverse_lazy("appprincipal:index")
    # def get (self, request):

    #     return render(request, self.template_name)
	

class Cadast_TipoUsersCreateView(CreateView):
    template_name = "registration/tipo_user.html"
    model = Tipo_Usuario
    form_class = RegistrarTipoUserForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
	#@method_decorator(allowed_users(allowed_roles=['admin', 'super']))

    def get (self, request):

        return render(request, self.template_name)

class Cadast_UserCreateView(CreateView):
    template_name = "instituicao/cadast_usuario.html"
    model = Usuario
    form_class = RegistrarUserForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
	#@method_decorator(allowed_users(allowed_roles=['admin', 'super']))
    def get (self, request):

        return render(request, self.template_name)




