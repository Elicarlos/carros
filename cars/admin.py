from django.contrib import admin
from . models import Car, Brand

class BranAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)
    

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BranAdmin)