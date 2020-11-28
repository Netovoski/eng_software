from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
import requests

# Create your views here.



class IndexTemplateView(TemplateView):
    template_name = "index.html"
    
    def get (self, request):
        return render(request, self.template_name)