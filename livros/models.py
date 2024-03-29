from django.db import models

class Genero(models.TextChoices):
    DRAMA = "DRAMA"
    ROMANCE = "ROMANCE"
    EPICO = "EPICO"
    AVENTURA = "AVENTURA"
    DISTOPIA = "DISTOPIA"
    CONTO = "CONTO"
    FANTASIA = "FANTASIA"
    SOBRENATURAL = "SOBRENATURAL"
    TERROR = "TERROR"
    DEFAULT = "NEUTRO"

class Book(models.Model):
    class Meta:
        ordering = ['id']
        
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    number_pages = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices=Genero.choices, default=Genero.DEFAULT)
    following = models.ManyToManyField('users.User', related_name='followed_books')


