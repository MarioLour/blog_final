from django import forms
from .models import Post,Comment,Category



class Modelo_Artigo(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Post
        fields = ('titulo', 'titulo_url', 'categorias', 'autor', 'corpo', 'imagem')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'categorias': forms.CheckboxSelectMultiple(),
            'titulo_url': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'corpo': forms.Textarea(attrs={'class': 'form-control'}),
 
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
        fields = ('nome','corpo')

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control','placeholder':'Nome'}),
            'corpo':forms.Textarea(attrs={'class':'form-control'}),

        }