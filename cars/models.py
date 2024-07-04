from django.db import models

# Criando a tabela referência de brand
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


# Criando a tabela do banco de dados dos carros
class Car(models.Model):
    id = models.AutoField(primary_key=True) 
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

# Após criar, usar o comando python manage.py makemigrations, criar o script para o banco de dados

# Depois, usar o comando python manage.py migrate, que vai varrer a aplicação, procurando os arquivos migrations e aplica atravez do ORM do django para o BD

    def __str__(self):
        return f'{self.brand} {self.model}'
