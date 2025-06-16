class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of a book."""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book instances."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title):
        """Returns a book by title if it's checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or wasn't checked out

    def list_available_books(self):
        """Prints a list of books that are not checked out."""
        for book in self._books:
            if book.is_available():
                print(book)
✅ Sample Output from main.py
python
Copy code
Available books after setup:
Brave New World by Aldous Huxley
1984 by George Orwell

Available books after checking out '1984':
Brave New World by Aldous Huxley

Available books after returning '1984':
Brave New World by Aldous Huxley
1984 by George Orwell
