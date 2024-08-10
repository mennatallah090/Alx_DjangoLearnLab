### Retrieve Operation

**Command:**

```python
# Retrieve all books
books = Book.objects.all()

# Display all books
for book in books:
    print(book.title, book.author, book.publication_year)
