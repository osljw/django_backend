from django.contrib import admin

from django.db import models
from markdownx.widgets import MarkdownxWidget
from django_json_widget.widgets import JSONEditorWidget

from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "question", "options", "url", "answer", "tip"]

    def formfield_for_dbfield(self, db_field, **kwargs):
        print("db_field:", db_field, kwargs.get('instance'))
        if db_field.name == 'options':
            kwargs['widget'] = JSONEditorWidget
        elif db_field.name == 'question':
            kwargs['widget'] = MarkdownxWidget
        # elif db_field.name == 'answer':
        #     # if kwargs.get('instance') and kwargs['instance'].type == 'multi_choice':
        #     kwargs['widget'] = JSONEditorWidget
        return super().formfield_for_dbfield(db_field, **kwargs)
    

admin.site.register(Question, QuestionAdmin)