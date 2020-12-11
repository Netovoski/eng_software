from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path
#from django.contrib.auth import views 
from appprincipal.registration.views import *


app_name = 'registration'



urlpatterns = [
    

    path('logout/', views.logoutUser, name = "logout"),
    path('login/', views.loginPage, name = "login"),
    path('register/', views.registerPage, name = "register"),
    path('registrar/', RegistrationTemplateView.as_view(), name = "registrar"),
    path('cria_users/', UsuariosCriarTemplateView.as_view(), name = "cria_users"),
    path('cria_userssuper/', UsuariosCriarSuperTemplateView.as_view(), name = "cria_userssuper"),
    path('usuarios/', views.UsersListView, name = "usuarios"),
    path('deletar/<pk>', UsuarioDeleteView.as_view(), name = "deletar"),
    path('profile/', views.profileUpdate, name='profile'),
    path('usuarios/<pk>', UsersUpdateView.as_view(), name = 'update_users'),
    

    # path('reset_senha/', views.PassowordResetView, name = 'reset_senha'),
    # path('reset_senha/done', views.PassowordResetDoneView, name = 'reset_senha_done'),
    # path('reset/<uidb64>/token/', views.PassowordResetConfirmView, name = 'reset_senha_confirm'),
    # path('reset/done', views.PassowordResetCompleteView, name = 'reset_senha_confirm'),
    


]