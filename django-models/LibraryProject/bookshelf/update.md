### Update Operation

**Command:**

```python
# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)
