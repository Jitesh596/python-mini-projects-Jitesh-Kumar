"""
Library Inventory Manager
Name: Jitesh kumar
Roll no: 2501010180
Course: Programming for Problem Solving using Python
"""


import json
from pathlib import Path

FILE = Path("library.json")

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.author} - {self.isbn} - {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "issued":
            return False
        self.status = "issued"
        return True

    def return_book(self):
        if self.status == "available":
            return False
        self.status = "available"
        return True

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.isbn == book.isbn:
                return False
        self.books.append(book)
        return True

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if not self.books:
            print("No books available.")
            return
        print("\nLibrary Books:")
        for b in self.books:
            print(b)

    def save(self):
        data = [b.to_dict() for b in self.books]
        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def load(self):
        if not FILE.exists():
            return
        try:
            with open(FILE) as f:
                data = json.load(f)
                for d in data:
                    self.books.append(Book(d["title"], d["author"], d["isbn"], d["status"]))
        except:
            print("File error. Starting fresh.")

def main():
    lib = LibraryInventory()
    lib.load()

    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All")
        print("5. Search")
        print("6. Save & Exit")

        ch = input("Choose: ")

        if ch == "1":
            t = input("Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            book = Book(t, a, i)
            if lib.add_book(book):
                print("Book added.")
            else:
                print("Book already exists.")

        elif ch == "2":
            i = input("ISBN to issue: ")
            b = lib.search_by_isbn(i)
            if b and b.issue():
                print("Book issued.")
            else:
                print("Book not found or already issued.")

        elif ch == "3":
            i = input("ISBN to return: ")
            b = lib.search_by_isbn(i)
            if b and b.return_book():
                print("Book returned.")
            else:
                print("Book not found or not issued.")

        elif ch == "4":
            lib.display_all()

        elif ch == "5":
            opt = input("Search by title or isbn? (t/i): ")
            if opt == "t":
                name = input("Enter title: ")
                result = lib.search_by_title(name)
                for r in result:
                    print(r)
            else:
                i = input("ISBN: ")
                b = lib.search_by_isbn(i)
                print(b if b else "No book found.")

        elif ch == "6":
            lib.save()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
