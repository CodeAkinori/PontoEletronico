from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50, unique=True)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
