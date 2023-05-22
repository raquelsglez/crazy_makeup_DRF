# Django and DRF imports
from django.contrib import admin

# proof class imports
from .models import MakeupProduct


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [
            ('0-10', '0 - 10'),
            ('11-20', '11 - 20'),
            ('21-30', '21 - 30'),
            ('31-40', '31 - 40'),
            ('41-50', '41 - 50'),
            ('51-60', '51 - 60'),
        ]

    def queryset(self, request, queryset):

        if self.value():
            valores = self.value().split("-")
            queryset = queryset.filter(price__range=(valores[0], valores[1]))

        return queryset


@admin.register(MakeupProduct)
class MakeupProductAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    list_display = ('name', 'color', 'trademark', 'price', 'created_at', 'updated_at', 'deleted_at', 'active')
    list_filter = ('color', 'stock', PriceRangeFilter)
    search_fields = ('name', 'trademark')
