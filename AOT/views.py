from django.shortcuts import render
from django.views.generic import DetailView,ListView,TemplateView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

from .models import AOT

class About(TemplateView):
    template_name = 'about.html'

class AOTListView(ListView):
    model = AOT
    template_name = 'aot_list.html'

class AOTDetailView(DetailView):
    model = AOT
    template_name = 'aot_detail.html'
    success_url = reverse_lazy('AOT')
    fields = "__all__"


class AOTCreateView(CreateView):
    model = AOT
    template_name = 'aot_create.html'
    fields = ['name','purchaser','description','img_url']

class AOTUpdateView(UpdateView):
    model = AOT
    template_name = 'aot_update.html'
    fields = ['name','purchaser','description','img_url']
    success_url = reverse_lazy('AOT')

class AOTDeleteView(DeleteView):
    model = AOT
    template_name = 'aot_delete.html'
    success_url = reverse_lazy('AOT')

# Create your views here.



    
    