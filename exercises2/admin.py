# Django and DRF imports
from django.contrib import admin

# proof class imports
from .models import Building, Flat


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('street', 'number', 'color', 'n_floors', 'total_flats', 'created_at', 'updated_at',
                    'deleted_at', 'active')
    list_filter = ('color', 'n_floors')
    search_fields = ('street', 'number')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('floor', 'letter', 'n_rooms', 'n_bathrooms', 'building', 'square_meter', 'created_at',
                    'updated_at', 'deleted_at', 'active')
    list_filter = ('n_rooms', 'n_bathrooms')
    search_fields = ('floor', 'letter')