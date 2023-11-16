from django.urls import path
from .views import Home,Artigo,Editar_Artigo,Criar_Artigo,Excluir_Artigo,Comment

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('artigos/<int:pk>',Artigo.as_view(),name="Artigo"),
    path('criar_artigo/',Criar_Artigo.as_view(),name="criar"),
    path('artigos/editar/<int:pk>',Editar_Artigo.as_view(),name="editar"),
    path('artigos/<int:pk>/excluir',Excluir_Artigo.as_view(),name='excluir'),
    path('artigos/<int:pk>/comentarios',Comment.as_view(),name='criar_comentario'),
    # Outras URLs do aplicativo 'blog', se houver
]