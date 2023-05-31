from django.contrib import admin
from .models import ListJson
from .models import DocJsonFile


@admin.register(ListJson)
class ListJsonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date'
    )


@admin.register(DocJsonFile)
class DocJsonFileAdmin(admin.ModelAdmin):
    list = (
        'id',
        'json-file',
    )
