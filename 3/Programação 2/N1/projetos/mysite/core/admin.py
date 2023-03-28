from django.contrib import admin
from core.models import Pessoas
class PessoasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'idade']
    search_fields = ['nome']
    list_filter = ['idade']
    list_editable = ['telefone', 'idade']
admin.site.register(Pessoas, PessoasAdmin)
# Register your models here.
