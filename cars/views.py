from django.shortcuts import render
from cars.models import Car

# Create your views here.
def cars_view(request):
    cars = Car.objects.filter(model__contains='R') # Busca os dados no bd

    return render(
                request,
                'cars.html', 
                {'cars': cars}
                )