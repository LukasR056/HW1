from django.contrib import admin

# Register your models here.
from soccer import models


class ClubsAdmin(admin.ModelAdmin):
    list_display = ('name', 'founding_date','points','active','country')
    sortable_by = ('name',)
    search_fields = ('name',) ##ist auch eine liste
    list_filter = ['players']
    pass
admin.site.register(models.Club,ClubsAdmin)

class PlayerAdmin (admin.ModelAdmin):
    list_display = ('first_name','last_name','year_of_birth','scorrer_points')
    pass
admin.site.register(models.Player, PlayerAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass
admin.site.register(models.Country,CountryAdmin)