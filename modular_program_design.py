books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
]

def add_book(title, author, year):
    books.append({"title": title, "author": author, "year": year})

def search_books(query):
    return [book for book in books if query in book["title"] or query in book["author"]]

def display_books():
    for book in books:
        print(f"{book['title']} by {book['author']} ({book['year']})")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Books")
        print("3. Display All Books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter publication year: "))
            add_book(title, author, year)
            print(f"Book '{title}' added successfully.")
        elif choice == "2":
            query = input("Enter search query: ")
            results = search_books(query)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"{book['title']} by {book['author']} ({book['year']})")
            else:
                print("No books found matching the query.")
        elif choice == "3":
            display_books()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()