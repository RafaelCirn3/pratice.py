from django.db import models

class TodoList(models.Model):
    tarefa = models.CharField(max_length=20)
    choice_status = [
        ('Pronto', 'pronto'),
        ('Em Andamento' , 'Em Andamento'),
        ('Pendente', 'Pendente') ]
    status = models.CharField(choices=choice_status,max_length=12)


class Ferramenta(models.Model):
    tipo = models.CharField(max_length=30)
    raridade = models.CharField(max_length=30)
    
# Create your models here.

