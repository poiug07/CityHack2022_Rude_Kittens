from django.contrib import admin
from predict import models

@admin.register(models.DataFile)
class ThemeAdmin(admin.ModelAdmin):
    search_fields = ("name",)

# Register your models here.
admin.site.register(models.DataPrediction)