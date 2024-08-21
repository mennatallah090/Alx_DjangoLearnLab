### Create Operation

**Command:**

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Save the instance
book.save()

# Check if the book was created
print(book)
