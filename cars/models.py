from django.db import models

# Create your models here.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    
    def __str__(self):
        print(type(self))  # Check the type of the returned value
        return self.name
    

class Car(models.Model):
    id =  models.AutoField(primary_key=True)
    model = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.cars_count} - {self.car_value}'
    
    
    
