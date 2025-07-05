# Create an empty dictionary to store book details
books = {}

# Loop to get details of 5 books
for i in range(1, 6):
    print(f"\nEnter details for Book {i}:")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    cost = input("Cost: ")

    # Add each book using its number (or ISBN) as key
    books[f"Book{i}"] = {
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Cost": cost
    }

# Print all book details
print("\nDetails of 5 Books:")
for book_id, details in books.items():
    print(f"\n{book_id}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
