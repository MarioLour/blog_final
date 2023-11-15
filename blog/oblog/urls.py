from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/criar/', views.create_post, name='criar'),
    path('post/<int:pk>/', views.view_post, name='Artigo'),
    path('post/editar/<int:pk>/', views.edit_post, name='editar'),
    path('post/deletar/<int:pk>/', views.delete_post, name='excluir'),
    # Outras URLs do aplicativo 'blog', se houver
]