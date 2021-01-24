from django.contrib import admin
from .models import Personagens, TpCaracteristica, Caracterizacao


class CaracterizacaoInline(admin.TabularInline):
    model = Caracterizacao
    extra = 1
    # list_filter = ['id_projeto', 'id_funcao_colaborador_projeto']
    # list_display = ['id_colaborador', 'id_funcao_colaborador_projeto',
    #                 'ch_semanal', 'inicio_vigencia', 'fim_vigencia']
    # search_fields = ['id_colaborador__nome']
    #
    raw_id_fields = ['id_tp_caracteristica']


class PersonagensAdmin(admin.ModelAdmin):
    list_filter = ['especie']
    list_display = ['nome', 'sobrenome', 'apelido', 'idade', 'casa']
    search_fields = ['nome', 'sobrenome', 'apelido']
    inlines = [CaracterizacaoInline]
    # raw_id_fields = ('id_projeto', 'id_colaborador', 'id_user_cad', 'id_user_alt')
    # fieldsets = (
    #     ('Projeto', {'fields': ['id_projeto']}),
    #     ('Participação do colaborador', {'fields': (('id_colaborador', 'id_funcao_colaborador_projeto'),
    #                                                 ('inicio_vigencia', 'fim_vigencia'), ('ch_semanal', 'valor'),)}),
    #     ('Outros', {'fields': (('id_user_cad'), ('id_user_alt', 'dt_alt'))})
    # )


admin.site.register(Personagens, PersonagensAdmin)
admin.site.register(TpCaracteristica)
admin.site.register(Caracterizacao)
