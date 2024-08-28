# CRUD Operations Documentation

## Create Operation
# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected Output: <Book: 1984>


## Retrieve Operation
# Retrieve Operation

```python
book = Book.objects.get(title="1984")
# Expected Output: <Book: 1984> (title='1984', author='George Orwell', publication_year=1949)


## Update Operation
# Update Operation

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Expected Output: <Book: Nineteen Eighty-Four>


## Delete Operation
# Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected Output: Confirmation of deletion


