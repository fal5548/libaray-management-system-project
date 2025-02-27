import sys
import os
import mysql.connector

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from library import Library
from book import Book

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Data-user1',
    'database': 'db_librarymanagement',
}

def display_menu():
    """Display the main menu."""
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Books by Title")
    print("4. List All Books")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit")

def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            # Add Book
            try:
                book_id = int(input("Enter book ID: "))
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                genre = input("Enter book genre: ")
                release_year = int(input("Enter release year: "))
                isbn = input("Enter ISBN number: ")
                available_copies = int(input("Enter number of available copies: "))
                new_book = Book(book_id, title, author, genre, release_year, isbn, available_copies)
                library.add_book(new_book)
                print("Book added successfully.")
            except ValueError:
                print("Invalid input. Please enter valid data for numeric fields.")

        elif choice == '2':
            # Remove Book
            try:
                book_id = int(input("Enter book ID to remove: "))
                library.remove_book(book_id)
                print("Book removed successfully.")
            except ValueError:
                print("Please enter a valid integer for book ID.")

        elif choice == '3':
            # Search Books by Title
            title = input("Enter the book title to search: ")
            results = library.search_books(title=title)  # Only searching by title
            if results:
                print("Search Results:")
                for book in results:
                    print(book)
            else:
                print("No books found with that title.")

        elif choice == '4':
            # List All Books
            library.list_books()

        elif choice == '5':
            # Borrow Book
            try:
                book_id = int(input("Enter book ID to borrow: "))
                library.borrow_book(book_id)
                print("Book borrowed successfully.")
            except ValueError:
                print("Please enter a valid integer for book ID.")

        elif choice == '6':
            # Return Book
            try:
                book_id = int(input("Enter book ID to return: "))
                library.return_book(book_id)
                print("Book returned successfully.")
            except ValueError:
                print("Please enter a valid integer for book ID.")

        elif choice == '0':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()