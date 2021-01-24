from django.db import models

especies = [
            ('Humano', 'Humano'),
            ('Lobo', 'Lobo')
            ]
papel_familiar = [
    ('Pai', 'Pai'),
    ('Mãe', 'Mãe'),
    ('Filh@', 'Filh@'),
    ('Ti@', 'Ti@'),
    ('Pai', 'Pai')
]


class Personagens(models.Model):
    id_personagem = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    apelido = models.CharField(max_length=30, null=True, blank=True)
    especie = models.CharField(max_length=30, choices=especies)

    class Meta:
        ordering = ['nome']
        db_table = 'personagens\".\"Personagens'

    def casa(self):
        if self.membro.values():
            return list(self.membro.values('id_casa_id__nome_casa'))[0]['id_casa_id__nome_casa']
        else:
            return '-'

    def __str__(self):
        nick = '-'
        if self.apelido:
            nick = self.apelido
        return str(self.nome) + ' (' + str(nick) + ')'


class TpCaracteristica(models.Model):
    id_tp_caracteristica = models.AutoField(primary_key=True)
    tp_caracteristica = models.CharField(max_length=40)

    class Meta:
        ordering = ['tp_caracteristica']
        db_table = 'personagens\".\"TpCaracteristica'

    def __str__(self):
        return str(self.tp_caracteristica)


class Caracterizacao(models.Model):
    id_caracterizacao = models.AutoField(primary_key=True)
    id_personagem = models.ForeignKey(Personagens, on_delete=models.CASCADE)
    id_tp_caracteristica = models.ForeignKey(TpCaracteristica, on_delete=models.CASCADE)
    caracteristica = models.CharField(max_length=50)

    class Meta:
        ordering = ('id_tp_caracteristica', 'caracteristica')
        db_table = 'personagens\".\"Caracterizacao'

    def __str__(self):
        return str(self.caracteristica) + ' - ' + str(self.id_tp_caracteristica)