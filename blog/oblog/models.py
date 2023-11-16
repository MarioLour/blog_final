from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_url = models.CharField(max_length=255,default="post")
    imagem = models.ImageField(null=True,blank=True,upload_to="images/")
    autor = models.ForeignKey(User , on_delete=models.CASCADE)
    corpo = models.TextField()
    data_publicada = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=255)
    

    def __str__(self):
        return self.titulo + '|' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post , related_name="Comentarios" , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)