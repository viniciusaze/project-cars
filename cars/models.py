from django.db import models

# Criando a tabela do banco de dados dos carros
class Car(models.Model):
    id = models.AutoField(primary_key=True) # AutoField = Autoincremeto
    model = models.CharField(max_length=200) # Charfield = String
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True) # IntegerField = Inteiro
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True) # FloatField = Float