# Update Operation

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Expected Output: <Book: Nineteen Eighty-Four>

