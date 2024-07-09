from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model') 
    # Busca todos os dados no bd
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search)
        # Busca os dados no bd com filtro

    return render(
                request,
                'cars.html', 
                {'cars': cars}
                )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES) # Para pegar os dados da requisição
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
                request,
                'new_car.html',
                {'new_car_form': new_car_form }
                )