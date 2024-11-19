from django.contrib import admin

from .models import Book, Borrow

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
admin.site.register(Book, BookAdmin)

class BorrowAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Borrow._meta.fields]
admin.site.register(Borrow, BorrowAdmin)