from django.contrib import admin
from cars.models import Car
from cars.models import Brand

# Adicionando o modelo Car na sessão admin
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registrando no admin
admin.site.register(Car, CarAdmin) # Parametros = Model e Admin
admin.site.register(Brand, BrandAdmin)