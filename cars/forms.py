from django import forms
from cars.models import Brand


class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) # Lista todas as marcas cadastradas
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()


