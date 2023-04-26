from django.contrib import admin

from django.db import models
from markdownx.widgets import MarkdownxWidget
from django_json_widget.widgets import JSONEditorWidget

from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "question", "options", "url", "answer", "tip"]
    # list_filter = ('created_time',)
    # search_fields = ('title', 'body')
    # ordering = ('-created_time',)
    # formfield_overrides = {
    #     models.TextField: {'widget': JSONEditorWidget},
    # }

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'options':
            kwargs['widget'] = JSONEditorWidget
        elif db_field.name == 'question':
            kwargs['widget'] = MarkdownxWidget
        return super().formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Question, QuestionAdmin)