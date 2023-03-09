from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.SlackMessage)
class SlackMessageAdmin(admin.ModelAdmin):
    list_display = ('Name', 'RecordType', 'Tag','Type', 'TypeCode',
                    'MessageStream', 'Description', 'From', 'Email', 'BouncedAt',)
    list_display_links = ('Name',)
    readonly_fields = ('BouncedAt',)
