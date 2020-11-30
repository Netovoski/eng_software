from django.shortcuts import render

# Create your views here.


class Cadast_CursoCreateView):
    template_name = "#"
    model = Curso
    form_class = RegistrarTipoCursoForm
    success_url = reverse_lazy("appprincipal:index")
    #@method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

@login_required
def CursoListView(ListView):
    curso = Curso.objects.all()
    
    contexto = {
        'curso': curso
    }

    return render(ListView, "#",contexto)


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "#"
    model = Curso
    fields = '__all__'
    context_object_name = "curso"
    success_url = reverse_lazy("#")
    # @method_decorator(login_required)
    # #@method_decorator(allowed_users(allowed_roles=['admin','gerente']))
    # def get (self, request):

    #     return render(request, self.template_name)


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "#"
    model = Curso
    context_object_name =  'Curso'
    #success_url = reverse_lazy("appprincipal:lista_produto")
    #@method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get_success_url (self):

        return reverse("#)

