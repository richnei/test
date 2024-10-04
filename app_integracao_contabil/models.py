from django.db import models

class IntegracaoContabil(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField()

    def __str__(self):
        return self.descricao
    
#trocar as variaveis dps