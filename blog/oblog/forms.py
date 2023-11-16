from django import forms
from .models import Post,Comment



class Modelo_Artigo(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','titulo_url','autor','corpo','imagem')

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
            'titulo_url':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.Select(attrs={'class':'form-control'}),
            'corpo':forms.Textarea(attrs={'class':'form-control'}),

        }
class Artigo_Editado(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','titulo_url','corpo')

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
            'titulo_url':forms.TextInput(attrs={'class':'form-control'}),
            'corpo':forms.Textarea(attrs={'class':'form-control'}),

        }

class Comentario_Editado(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

        }