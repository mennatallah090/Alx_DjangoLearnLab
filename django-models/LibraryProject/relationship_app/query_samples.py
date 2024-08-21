from relationship_app.models import Author,Book,Library,Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def librarian_for_library(library_name):
    library= Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Example usage
if __name__ == "__main__":
    print("Books by Author:")
    for book in books_by_author("Author Name"):
        print(book.title)

    print("\nBooks in Library:")
    for book in books_in_library("Library Name"):
        print(book.title)

    print("\nLibrarian for Library:")
    librarian = librarian_for_library("Library Name")
    print(librarian.name)