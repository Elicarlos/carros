


from django import forms

from cars.models import Brand, Car


class CarForms(forms.Form):
    model = forms.CharField(max_length=250)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.CharField(max_length=250)
    model_year = forms.CharField(max_length=250)
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
    
    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo']
        )
        car.save()
        return car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        
        if value < 20000:
            self.value.add_error("value", "Valor minino deve ser de 20.000")
        
        return value
    
    
    