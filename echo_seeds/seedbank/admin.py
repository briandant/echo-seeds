from django.contrib import admin

from models import (
    Seed, Location, Family,
    ScientificName, CommonName,
    Variety, Germination,
    Supplier, SupplierType,
)


class SeedAdmin(admin.ModelAdmin):

    list_display = (
        '__unicode__', 'scientific_name', 'family',
        'common_name', 'variety', 'acquisition_location'
    )

    search_fields = ('accession_num', 'lot_num',
                     'common_name__name', 'scientific_name__name'
                     )


class LocationAdmin(admin.ModelAdmin):

    list_display = ('name', 'code', 'type')
    search_fields = ('name', 'code')


class CommonNameAdmin(admin.ModelAdmin):

    list_display = ('name', 'scientific_name')
    search_fields = ('name', 'scientific_name__name')


admin.site.register(Seed, SeedAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Family)
admin.site.register(ScientificName)
admin.site.register(CommonName, CommonNameAdmin)
admin.site.register(Variety)
admin.site.register(Germination)
admin.site.register(Supplier)
admin.site.register(SupplierType)
