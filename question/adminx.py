import xadmin

from .models import Question


class QuestionAdmin:
    list_display = ["id", "type", "question", "url", "answer", "tip"]
xadmin.site.register(Question, QuestionAdmin)
