from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path


from appprincipal.curso.views import *

app_name = 'curso'

urlpatterns = [
    path('curso_cadast/', Cadast_CursoCreateView.as_view(), name="curso_cadast"),
    #path('tipoprod/produto/', Cadast_ProdCreateView.as_view(), name = 'produto'),
    #path('produto/', ListaProdutoListView.as_view(), name = 'lista_produto'),
    path('curso/', views.CursoListView, name = "lista_curso"),
    path('curso/<pk>', CursoUpdateView.as_view(), name = 'update_curso'),
    path('curso/excluir/<pk>', CursoDeleteView.as_view(), name = 'deleta_curso'),
    path('cursoacesso/', CursoTemplateView.as_view(), name = "curso_acesso"),

]