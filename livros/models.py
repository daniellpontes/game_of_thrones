from django.db import models
from personagens.models import Personagens

paises = [('BR', 'Brasil'),
            ('USA', 'Estados Unidos')
          ]


class Editoras(models.Model):
    id_editora = models.AutoField(primary_key=True)
    editora = models.CharField(max_length=30)
    razao_social = models.CharField(max_length=50, null=True, blank=True)
    pagina = models.URLField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['editora']
        db_table = 'livros\".\"Editoras'

    def __str__(self):
        return self.editora


class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70)
    ano_nascimento = models.IntegerField()
    pais_nascimento = models.CharField(max_length=3, choices=paises)
    pagina = models.URLField()
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 'livros\".\"Autores'

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    id_editora = models.ForeignKey(Editoras, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=80)
    isbn = models.CharField(max_length=20)
    edicao_numero = models.IntegerField()
    edicao_ano = models.IntegerField()
    num_paginas = models.IntegerField()

    class Meta:
        ordering = ['titulo']
        db_table = 'livros\".\"Livros'

    def __str__(self):
        return self.titulo


class Capitulos(models.Model):
    id_capitulo = models.AutoField(primary_key=True)
    id_livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    num_capitulo = models.IntegerField()
    nome_capitulo = models.CharField(max_length=30, null=True, blank=True)
    pagina_inicio = models.IntegerField()
    pagina_termino = models.IntegerField()

    class Meta:
        ordering = ['num_capitulo']
        db_table = 'livros\".\"Capitulos'

    def __str__(self):
        return str(self.num_capitulo) + ' - ' + str(self.nome_capitulo)


class Eventos(models.Model):
    id_evento = models.AutoField(primary_key=True)
    id_capitulo = models.ForeignKey(Capitulos, on_delete=models.CASCADE)
    valor_inicial = models.CharField(max_length=50)
    valor_final = models.CharField(max_length=50)

    class Meta:
        ordering = ['id_evento']
        db_table = 'livros\".\"Eventos'

    def __str__(self):
        return str(self.valor_final) + ' - ' + str(self.valor_final)


"""
class Beats(models.Model):
    id_beat = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    beat = models.CharField(max_length=255)
        

class ParticipantesBeats(models.Model):
    id_participante_beats = models.AutoField(primary_key=True)
    id_beat = models.ForeignKey(Beats, on_delete=models.CASCADE)
    id_personagem = models.ForeignKey(Personagens, on_delete=models.CASCADE)
"""