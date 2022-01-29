from django.contrib import admin
from .models import *


class DisplayConfigReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Receita, DisplayConfigReceitas)
admin.site.register(Categoria)