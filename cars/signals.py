from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    # Salvando os registros
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


def limit_car_inventory():
    max_objects = 200
    if CarInventory.objects.count() > max_objects:
        oldest_object = CarInventory.objects.order_by('created_at').first()
        oldest_object.delete()

# Incluindo os signals
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = f''' O usuário não informou descrição para o carro
        {instance.brand} {instance.model} - {instance.model_year}'''

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
    limit_car_inventory()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
    limit_car_inventory()