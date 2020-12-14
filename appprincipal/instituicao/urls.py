from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path


from appprincipal.instituicao.views import *

app_name = 'instituicao'

urlpatterns = [
    # path('cria_instituicao/', InstituicaoCreateView.as_view(), name="cria_instituicao"),
    # path('cria_dirigente/', DirigenteCreateView.as_view(), name="cria_dirigente"),
    path('institucional/', InstituicaoTemplateView.as_view(), name = "institucional"),
    path('cria_instpar/', Cadast_InstParCreateView.as_view(), name="cria_instpar"),
    path('cria_instval/', Cadast_InstValCreateView.as_view(), name="cria_instval"),
    
    path('update_instpar/<pk>', Update_InstParUpdateView.as_view(), name="update_instpar"),
    path('update_instval/<pk>', Update_InstValUpdateView.as_view(), name="update_instval"),

    path('cria_dirigentepar/', Cadast_DirigenteParCreateView.as_view(), name="cria_dirigentepar"),
    path('cria_dirigenteval/', Cadast_DirigenteValCreateView.as_view(), name="cria_dirigenteval"),
    
    
    path('cria_diretor/', Cadast_DiretorParCreateView.as_view(), name="cria_diretor"),
    path('cria_superval/', Cadast_SuperValCreateView.as_view(), name="cria_super"),

    path('cria_func/', Cadast_FuncionarioCreateView.as_view(), name="cria_func"),

    path('instpar/', views.InstParListView, name = "lista_instpar"),
    path('instval/', views.InstValListView, name = "lista_instval"),

    
]