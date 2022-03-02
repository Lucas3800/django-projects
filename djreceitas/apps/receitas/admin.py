from django.contrib import admin
from .models import *


class DisplayConfigReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'publicar')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria',)
    search_fields = ('nome',)
    list_per_page = 10
    list_editable = ('publicar',)

admin.site.register(Receita, DisplayConfigReceitas)
admin.site.register(Categoria)