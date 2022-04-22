from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Type', 'Year')
    list_filter = ['Year']
    search_fields = ['Name', 'Type']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('Name', 'Description')
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)