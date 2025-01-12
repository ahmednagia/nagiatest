# Define the Book class
class Book:
    def __init__(self, title, author):
        # Initialize attributes
        self.title = title
        self.author = author
        self.available = True  # All books are available when added to the catalogue

    def check_out(self):
        """Method to check out a book. Updates availability status."""
        if self.available:
            self.available = False
            print(f'You have checked out "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is currently unavailable.')

    def return_book(self):
        """Method to return a book. Updates availability status."""
        if not self.available:
            self.available = True
            print(f'You have returned "{self.title}".')
        else:
            print(f'"{self.title}" was not checked out.')

    def __str__(self):
        """Returns a string representation of the book."""
        status = 'Available' if self.available else 'Checked Out'
        return f'"{self.title}" by {self.author} - {status}'


# Define the Library class
class Library:
    def __init__(self):
        self.books = []  # List to store books in the catalogue

    def add_book(self, title, author):
        """Method to add a new book to the catalogue."""
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Added "{title}" by {author} to the catalogue.')

    def view_books(self):
        """Method to view all books in the catalogue."""
        if not self.books:
            print('No books in the catalogue.')
        for book in self.books:
            print(book)


# Main code to simulate the library system
def main():
    # Create a new library
    library = Library()

    # Add new books to the library
    
