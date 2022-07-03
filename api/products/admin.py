from django.contrib import admin
from . import models


@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'id', 'status', 'slug', 'vendor')
    prepopulated_fields = {'slug': ('item_name',), }


admin.site.register(models.ProductType)
admin.site.register(models.WeatherType)
