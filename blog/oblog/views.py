from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpResponse


# Criar um post no blog


def home(request):
    posts = Post.objects.all().order_by('-data_publicada')  # Obtém todos os posts ordenados por data de publicação (do mais recente ao mais antigo)
    return render(request, 'home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        titulo_url = request.POST.get('titulo_url')
        autor = request.user  # Supondo que o usuário está autenticado
        corpo = request.POST.get('corpo')
        categoria = request.POST.get('categoria')
        imagem = request.FILES.get('imagem')  # Captura a imagem do formulário

        new_post = Post.objects.create(
            titulo=titulo,
            titulo_url=titulo_url,
            autor=autor,
            corpo=corpo,
            categoria=categoria,
            imagem=imagem  # Salva a imagem no novo post
        )
        return redirect('Artigo', pk=new_post.pk)  # Redireciona para a visualização do novo post
    return render(request, 'criar_artigo.html')

# Ver o post na própria página dele
def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'artigo.html', {'post': post})

# Editar o post tanto na página home quanto na página do post
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # Extrair os dados do POST
        titulo = request.POST.get('titulo')
        corpo = request.POST.get('corpo')
        categoria = request.POST.get('categoria')
        
        # Atualizar os dados do post com os novos dados recebidos
        post.titulo = titulo
        post.corpo = corpo
        post.categoria = categoria
        post.save(update_fields=['titulo', 'corpo', 'categoria'])  # Atualiza apenas os campos necessários

        # Redirecionar para a visualização do post atualizado
        return redirect('Artigo', pk=post.pk)
    return render(request, 'editar_artigo.html', {'post': post})

# Deletar o post tanto na página home quanto na página dele
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # Deletar o post
        post.delete()
        # Redirecionar para a página inicial do blog ou outra página desejada
        return redirect('home')
    return render(request, 'excluir_artigo.html', {'post': post})