import mysql.connector
from mysql.connector import Error
from book import Book

class Library:
    def __init__(self):
        self.connection = self.create_connection()
        self.create_books_table()
        self.create_libraries_table()

    def create_connection(self):
        """Create a database connection."""
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='db_librarymanagement',
                user='root',  # Replace with your MySQL username
                password='Data-user1'  # Replace with your MySQL password
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except Error as e:
            print(f"Error: '{e}'")
            return None

    def create_books_table(self):
        """Create the books table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            book_id INT PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            genre VARCHAR(255),
            release_year INT,
            isbn VARCHAR(20),
            available_copies INT
        );
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_table_query)
                print("Books table created successfully.")
        except Error as e:
            print(f"Error creating books table: '{e}'")

    def create_libraries_table(self):
        """Create the libraries table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS libraries (
            library_id INT AUTO_INCREMENT PRIMARY KEY,
            library_name VARCHAR(255) NOT NULL,
            location VARCHAR(255),
            established_year INT,
            contact_number VARCHAR(20),
            email VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_table_query)
                print("Libraries table created successfully.")
        except Error as e:
            print(f"Error creating libraries table: '{e}'")

    def add_book(self, book):
        """Add a new book to the library."""
        insert_query = """
        INSERT INTO books (book_id, title, author, genre, release_year, isbn, available_copies)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (book.book_id, book.title, book.author, book.genre,
                                               book.release_year, book.isbn, book.available_copies))
                self.connection.commit()
                print(f"Book '{book.title}' added to the library.")
        except Error as e:
            print(f"Error adding book: '{e}'")

    def remove_book(self, book_id):
        """Remove a book from the library by its ID."""
        delete_query = "DELETE FROM books WHERE book_id = %s;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(delete_query, (book_id,))
                self.connection.commit()
                if cursor.rowcount > 0:
                    print(f"Book with ID {book_id} removed from the library.")
                else:
                    print("Book not found.")
        except Error as e:
            print(f"Error removing book: '{e}'")

    def list_books(self):
        """List all books in the library."""
        select_query = "SELECT * FROM books;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query)
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No books available in the library.")
        except Error as e:
            print(f"Error listing books: '{e}'")

    def borrow_book(self, book_id):
        """Borrow a book from the library."""
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT available_copies FROM books WHERE book_id = %s;", (book_id,))
            result = cursor.fetchone()
            if result and result[0] > 0:
                update_query = "UPDATE books SET available_copies = available_copies - 1 WHERE book_id = %s;"
                cursor.execute(update_query, (book_id,))
                self.connection.commit()
                print(f"You have borrowed the book with ID {book_id}.")
            else:
                print("No copies available for borrowing or book not found.")
        except Error as e:
            print(f"Error borrowing book: '{e}'")
        finally:
            cursor.close()

    def return_book(self, book_id):
        """Return a book to the library."""
        update_query = "UPDATE books SET available_copies = available_copies + 1 WHERE book_id = %s;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(update_query, (book_id,))
                self.connection.commit()
                if cursor.rowcount > 0:
                    print(f"You have returned the book with ID {book_id}.")
                else:
                    print("Book not found.")
        except Error as e:
            print(f"Error returning book: '{e}'")

    def search_books(self, **kwargs):
        """Search for books based on given criteria."""
        if not kwargs:
            print("No search criteria provided.")
            return []

        results = []
        select_query = "SELECT * FROM books WHERE " + " AND ".join([f"{key} = %s" for key in kwargs.keys()])
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(select_query, tuple(kwargs.values()))
                rows = cursor.fetchall()
                for row in rows:
                    results.append(row)
        except Error as e:
            print(f"Error searching books: '{e}'")
        return results

    def close_connection(self):
        """Close the database connection."""
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")