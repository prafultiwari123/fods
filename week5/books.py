import csv
import os

class Book:
    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued  # True if issued, False if available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": str(self.is_issued)  # store as string for CSV
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["is_issued"].lower() == 'true'
        )

class Library:
    def __init__(self, filename="books.csv"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.filename):
            self.books = []
            return
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.books = [Book.from_dict(row) for row in reader]
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                fieldnames = ['book_id', 'title', 'author', 'is_issued']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for book in self.books:
                    writer.writerow(book.to_dict())
        except Exception as e:
            print(f"Error saving books: {e}")

    def add_book(self, book):
        if any(b.book_id == book.book_id for b in self.books):
            print(f"Book ID {book.book_id} already exists.")
            return
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added successfully.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    print(f"Book '{book.title}' is already issued.")
                else:
                    book.is_issued = True
                    self.save_books()
                    print(f"Book '{book.title}' issued successfully.")
                return
        print(f"No book found with ID {book_id}.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    print(f"Book '{book.title}' was not issued.")
                else:
                    book.is_issued = False
                    self.save_books()
                    print(f"Book '{book.title}' returned successfully.")
                return
        print(f"No book found with ID {book_id}.")

    def search_book(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if not found_books:
            print(f"No books found matching '{keyword}'.")
        else:
            print(f"Books matching '{keyword}':")
            for book in found_books:
                status = "Issued" if book.is_issued else "Available"
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\nLibrary Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Display All Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == '2':
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == '3':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '4':
            keyword = input("Enter title or author to search: ")
            library.search_book(keyword)

        elif choice == '5':
            library.display_all_books()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
