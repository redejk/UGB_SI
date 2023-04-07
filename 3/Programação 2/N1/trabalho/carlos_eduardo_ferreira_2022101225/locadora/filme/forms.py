from django.forms import ModelForm
from .models import Filmes, Generos

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = '__all__'

class GenerosForm(ModelForm):
    class Meta:
        model = Generos
        fields = '__all__'