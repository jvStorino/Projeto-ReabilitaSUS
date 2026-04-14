from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('nome', 'email', 'mensagem')
