class Book:
    def __init__(self, book_id, title, author, genre, release_year, isbn, available_copies):
        self.book_id = book_id  # Unique identifier for the book
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.genre = genre  # Genre of the book
        self.release_year = release_year  # Release year of the book
        self.isbn = isbn  # ISBN number of the book
        self.available_copies = available_copies  # Number of copies available
        self.checked_out = 0  # Number of copies currently checked out

    def check_out(self):
        """Check out the book and update the available copies."""
        if self.available_copies > 0:
            self.available_copies -= 1
            self.checked_out += 1
            print(f"You have checked out: {self.title}")
        else:
            print("No copies available for checkout.")

    def return_book(self):
        """Return the book and update the available copies."""
        if self.checked_out > 0:
            self.available_copies += 1
            self.checked_out -= 1
            print(f"You have returned: {self.title}")
        else:
            print("This book was not checked out.")

    def __str__(self):
        """String representation of the book."""
        return (f"{self.title} by {self.author} (ID: {self.book_id}, "
                f"ISBN: {self.isbn}, Available Copies: {self.available_copies})")

    def details(self):
        """Return detailed information about the book."""
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Genre: {self.genre}\n"
                f"Release Year: {self.release_year}\n"
                f"ISBN: {self.isbn}\n"
                f"Available Copies: {self.available_copies}\n"
                f"Checked Out: {self.checked_out}")