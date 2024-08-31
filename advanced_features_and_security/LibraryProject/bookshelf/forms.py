# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search Books')

# Example of a form for adding or updating books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Assuming you have a Book model
        fields = ['title', 'author', 'published_date', 'isbn']
# LibraryProject/bookshelf/forms.py


class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100, label='Example Field')
