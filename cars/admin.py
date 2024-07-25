from django.contrib import admin
from cars.models import Car, Brand, CarInventory


# Adicionando o modelo Car na sessão admin
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarInvetoryAdmin(admin.ModelAdmin):
    list_display = ('cars_count', 'cars_value', 'created_at')
    search_fields = ('created_at',)

# Registrando no admin
admin.site.register(Car, CarAdmin) # Parametros = Model e Admin
admin.site.register(Brand, BrandAdmin)
admin.site.register(CarInventory, CarInvetoryAdmin)