from django.contrib import admin
from predict import models

@admin.register(models.DataFile)
class DataFileAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(models.DataPrediction)
class DataPredictionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": ("datafile_id", "predictionsJSON"),
            },
        ),
    )