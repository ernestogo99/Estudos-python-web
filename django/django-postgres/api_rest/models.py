from django.db import models
import uuid

class Interprete(models.Model):
    cod_inter=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nome=models.CharField(max_length=255,null=False,blank=False,default='')
    tipo=models.CharField(max_length=255,null=False,blank=False,default='')

    def __str__(self):
        return f'nome: {self.nome} | tipo: {self.tipo}'
