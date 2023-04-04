from django.forms import ModelForm
from .models import Discos

class DiscosForm(ModelForm):
    class Meta:
        model = Discos
        #fields = '__all__' = Todos
        #fields = [''] = Somente os que selecionar
        #exclude = ['preco'] = Todos menos o especificado
        #obs só é possível usar fields ou exclude, nunca os dois juntos
        fields = '__all__'
