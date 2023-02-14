from django.contrib import admin

# Register your models here.

from .models import Car, Type_of_car

@admin.register(Car)
class Caradmin(admin.ModelAdmin):
    list_display = ['model', 'type_of_car', 'age', 'color']

@admin.register(Type_of_car)
class Type_of_caradmin(admin.ModelAdmin):
    ...