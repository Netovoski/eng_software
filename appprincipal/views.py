from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
import requests
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
import json
import datetime
# Create your views here.
from django.views import generic
import requests
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views

class IndexTemplateView(TemplateView):
    template_name = "index.html"
    @method_decorator(login_required, allowed_users(allowed_roles=['customer']))
    def get (self, request):
        return render(request, self.template_name)