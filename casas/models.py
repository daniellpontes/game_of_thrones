from django.db import models
from personagens.models import Personagens


papel_casa = [
    ('Rei', 'Rei'),
    ('Rainha', 'Rainha'),
    ('Príncipe herdeiro', 'Príncipe herdeiro'),
    ('Príncipe', 'Príncipe'),
    ('Princesa', 'Princesa'),
    ('Sem papel definido', 'Sem papel definido')
]


class Casas(models.Model):
    id_casa = models.AutoField(primary_key=True)
    nome_casa = models.CharField(max_length=30)
    lema = models.CharField(max_length=60, null=True, blank=True)
    simbolo = models.ImageField(upload_to="imagens", null=True, blank=True)

    class Meta:
        ordering = ['nome_casa']
        db_table = 'casas\".\"Casas'

    def __str__(self):
        return self.nome_casa


class Membros(models.Model):
    id_membro = models.AutoField(primary_key=True)
    id_casa = models.ForeignKey(Casas, on_delete=models.CASCADE)
    id_personagem = models.ForeignKey(Personagens, on_delete=models.CASCADE, related_name='membro')
    papel_casa = models.CharField(max_length=50, null=True, blank=True, choices=papel_casa)

    class Meta:
        ordering = ['id_membro']
        db_table = 'casas\".\"Membros'

    def __str__(self):
        return str('id_perssonagem.nome')


class Caracteristicas(models.Model):
    id_caracteristica = models.AutoField(primary_key=True)
    id_casa = models.ForeignKey(Casas, on_delete=models.CASCADE)
    caracteristica = models.CharField(max_length=250)

    class Meta:
        ordering = ['id_caracteristica']
        db_table = 'casas\".\"Caracteristicas'

    def __str__(self):
        return self.caracteristica
