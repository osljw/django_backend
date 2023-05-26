from django.contrib import admin

from django.db import models
from markdownx.widgets import MarkdownxWidget
from django_json_widget.widgets import JSONEditorWidget

from .models import Travel, City
# Register your models here.

class TravelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Travel._meta.fields]

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     print("db_field:", db_field, kwargs.get('instance'))
    #     if db_field.name == 'options':
    #         kwargs['widget'] = JSONEditorWidget
    #     elif db_field.name == 'question':
    #         kwargs['widget'] = MarkdownxWidget
    #     # elif db_field.name == 'answer':
    #     #     # if kwargs.get('instance') and kwargs['instance'].type == 'multi_choice':
    #     #     kwargs['widget'] = JSONEditorWidget
    #     return super().formfield_for_dbfield(db_field, **kwargs)
    

admin.site.register(Travel, TravelAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in City._meta.fields]

admin.site.register(City, CityAdmin)