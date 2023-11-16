from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  # Importe o formulário que será criado

def home(request):
    posts = Post.objects.all().order_by('-data_publicada')
    return render(request, 'home.html', {'posts': posts})

from django.contrib.auth.models import User

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.autor = request.user
            new_post.save()
            return redirect('Artigo', pk=new_post.pk)
    else:
        form = PostForm()
    return render(request, 'criar_artigo.html', {'form': form})

def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Artigo.html', {'post': post})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('Artigo', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'editar_artigo.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'excluir_artigo.html', {'post': post})