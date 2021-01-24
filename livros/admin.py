from django.contrib import admin
from .models import Editoras, Autores, Livros, Capitulos


class CapitulosAdmin(admin.ModelAdmin):
    list_filter = ['id_livro__titulo']
    list_display = ['num_capitulo', 'nome_capitulo', 'pagina_inicio', 'pagina_termino']
    search_fields = ['nome_capitulo']
    # raw_id_fields = ('id_projeto', 'id_colaborador', 'id_user_cad', 'id_user_alt')
    # fieldsets = (
    #     ('Projeto', {'fields': ['id_projeto']}),
    #     ('Participação do colaborador', {'fields': (('id_colaborador', 'id_funcao_colaborador_projeto'),
    #                                                 ('inicio_vigencia', 'fim_vigencia'), ('ch_semanal', 'valor'),)}),
    #     ('Outros', {'fields': (('id_user_cad'), ('id_user_alt', 'dt_alt'))})
    # )


admin.site.register(Editoras)
admin.site.register(Autores)
admin.site.register(Livros)
admin.site.register(Capitulos, CapitulosAdmin)