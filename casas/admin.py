from django.contrib import admin
from .models import *


class MembrosInline(admin.TabularInline):
    model = Membros
    extra = 1
    # list_filter = ['id_projeto', 'id_funcao_colaborador_projeto']
    # list_display = ['id_colaborador', 'id_funcao_colaborador_projeto',
    #                 'ch_semanal', 'inicio_vigencia', 'fim_vigencia']
    # search_fields = ['id_colaborador__nome']
    #
    raw_id_fields = ['id_personagem']


class CaracteristicasInline(admin.TabularInline):
    model = Caracteristicas
    extra = 1


class CasasAdmin(admin.ModelAdmin):
    # list_filter = ('id_projeto', 'id_funcao_colaborador_projeto')
    list_display = ('nome_casa', 'lema')
    search_fields = ['nome_casa']
    inlines = [MembrosInline, CaracteristicasInline]
    # raw_id_fields = ('id_projeto', 'id_colaborador', 'id_user_cad', 'id_user_alt')
    # fieldsets = (
    #     ('Projeto', {'fields': ['id_projeto']}),
    #     ('Participação do colaborador', {'fields': (('id_colaborador', 'id_funcao_colaborador_projeto'),
    #                                                 ('inicio_vigencia', 'fim_vigencia'), ('ch_semanal', 'valor'),)}),
    #     ('Outros', {'fields': (('id_user_cad'), ('id_user_alt', 'dt_alt'))})
    # )


admin.site.register(Casas, CasasAdmin)
# admin.site.register(Membros)
