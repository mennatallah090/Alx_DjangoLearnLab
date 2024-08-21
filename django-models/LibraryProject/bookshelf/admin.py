from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in list view
    list_filter = ('publication_year', 'author')            # Filters to apply on the right sidebar
    search_fields = ('title', 'author')                     # Searchable fields

# Alternatively, you can register the model without the decorator:
# admin.site.register(Book, BookAdmin)