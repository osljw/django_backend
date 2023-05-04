from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    # list_filter = ('is_active', )
    search_fields = ('title', )

admin.site.register(Notice, NoticeAdmin)