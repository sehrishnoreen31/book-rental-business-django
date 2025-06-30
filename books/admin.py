from django.contrib import admin
from .models import Book, BookTitle
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('book_id', 'qr_code')

@admin.register(BookTitle)
class BookTitleAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)