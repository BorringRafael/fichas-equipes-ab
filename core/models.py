from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Unidade(models.Model):
    # Tabela de unidades cadastradas.
    nome = models.CharField(
        'Nome',
        max_length=256,
        )
    cnes = models.CharField(
        'CNES',
        max_length=7,
        validators=[
                    MaxLengthValidator(7, 'São 7 dígitos'),
                    MinLengthValidator(7, 'São 7 dígitos'),
                    ],
        unique=True,
        )

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return '%s - %s' % (self.cnes, self.nome)


class Equipe(models.Model):
    # Tabela de equipes da AB.
    nome = models.CharField(
        'Nome',
        max_length=256,
        )
    area = models.CharField(
        'Área',
        max_length=4,
        validators=[
                    MaxLengthValidator(4, 'São 4 dígitos'),
                    MinLengthValidator(4, 'São 4 dígitos'),
                    ],
        unique=True,
        blank=True,
        )
    ine = models.CharField(
        'INE',
        max_length=10,
        validators=[
                    MaxLengthValidator(10, 'São 10 dígitos'),
                    MinLengthValidator(10, 'São 10 dígitos'),
                    ],
        unique=True,
        )
    unidade = models.ForeignKey(
        'Unidade',
        )

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return '%s - %s' % (self.area, self.nome)


class Profissional(models.Model):
    # Tabela de profissionais da AB.
    nome = models.CharField(
        'Nome',
        max_length=256,
        )
    cns = models.CharField(
        'CNS',
        max_length=15,
        validators=[
                    MaxLengthValidator(15, 'São 15 dígitos'),
                    MinLengthValidator(15, 'São 15 dígitos'),
                    ],
        unique=True,
        )
    cbo = models.ForeignKey(
        'CBO',
        )
    equipe = models.ForeignKey(
        'Equipe',
        blank=True,
        )

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'profissionais'

    def __str__(self):
        return '%s - %s' % (self.nome, self.cbo.nome)


class CBO(models.Model):
    # Tabela de CBOs.
    nome = models.CharField(
        'Nome',
        max_length=256,
        )
    cbo = models.CharField(
        'CBO',
        max_length=6,
        validators=[
                    MaxLengthValidator(6, 'São 6 dígitos'),
                    MinLengthValidator(6, 'São 6 dígitos'),
                    ],
        unique=True,
        )

    class Meta:
        verbose_name = 'CBO'
        verbose_name_plural = 'CBOs'

    def __str__(self):
        return '%s - %s' % (self.cbo, self.nome)
