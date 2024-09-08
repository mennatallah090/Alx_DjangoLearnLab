from django.db import models


class Author(models.Model):
    """
    The Author model represents a book author with a name field.
    """
    # name: the name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a book with a title, publication year, and an associated author.
    """
    # title: the title of the book
    title = models.CharField(max_length=255)
    
    # publication_year: the year the book was published
    publication_year = models.IntegerField()
    
    # author: the author of the book, establishing a foreign key relationship
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title

