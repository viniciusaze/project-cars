from django import forms
from cars.models import Car
    

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    # Validações
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$10.000')
        return value
    

    def clean_factory_year(self):
        year = self.cleaned_data.get('factory_year')
        if year < 1970:
            self.add_error('factory_year', 'Ano mínimo do carro deve ser de 1970')
        return year