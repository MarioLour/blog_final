from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import Modelo_Artigo,Artigo_Editado
from django.urls import reverse_lazy



class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-data_publicada']




class Artigo(DetailView):
    model = Post
    template_name = "artigo.html"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except self.model.DoesNotExist:
            raise Http404("Post does not exist")
       
class Criar_Artigo(CreateView):
    model = Post
    form_class = Modelo_Artigo
    template_name = "criar_artigo.html"
    
class Editar_Artigo(UpdateView):
    model = Post
    template_name = "editar_artigo.html"
    form_class = Artigo_Editado

class Excluir_Artigo(DeleteView):
    model = Post
    template_name = 'excluir_artigo.html'
    success_url = reverse_lazy('home')