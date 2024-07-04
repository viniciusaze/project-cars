from django.shortcuts import render

# Create your views here.
def cars_view(request):
    return render(
                request,
                template_name='cars.html', 
                context={'cars': {'model':'Civic 1.7'}}
                )