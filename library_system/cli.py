from .storage import Storage
from .models import Book
from typing import List


def prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def list_books(storage: Storage):
    books = storage.load_books()
    if not books:
        print("No books in the library.")
        return
    print(f"{'ID':<4} {'Title':<30} {'Author':<20} {'Year':<6} {'Copies':<6}")
    for b in books:
        print(f"{b.id:<4} {b.title[:29]:<30} {b.author[:19]:<20} {str(b.year or ''):<6} {b.copies:<6}")


def add_book(storage: Storage):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year_input = input("Year (optional): ").strip()
    year = int(year_input) if year_input.isdigit() else None
    copies = prompt_int("Copies [1]: ") or 1
    book = Book(id=storage.next_id(), title=title, author=author, year=year, copies=copies)
    books = storage.load_books()
    books.append(book)
    storage.save_books(books)
    print(f"Added book ID {book.id}.")


def search_books(storage: Storage):
    q = input("Search by title/author: ").strip().lower()
    books = storage.load_books()
    results = [b for b in books if q in b.title.lower() or q in b.author.lower()]
    if not results:
        print("No matches.")
        return
    for b in results:
        print(f"{b.id}: {b.title} — {b.author} ({b.year}) [{b.copies} copies]")


def borrow_book(storage: Storage):
    bid = prompt_int("Book ID to borrow: ")
    books = storage.load_books()
    for b in books:
        if b.id == bid:
            if b.copies > 0:
                b.copies -= 1
                storage.save_books(books)
                print("Borrowed successfully.")
            else:
                print("No copies available.")
            return
    print("Book not found.")


def return_book(storage: Storage):
    bid = prompt_int("Book ID to return: ")
    books = storage.load_books()
    for b in books:
        if b.id == bid:
            b.copies += 1
            storage.save_books(books)
            print("Returned. Thank you.")
            return
    print("Book not found.")


def remove_book(storage: Storage):
    bid = prompt_int("Book ID to remove: ")
    books = storage.load_books()
    new = [b for b in books if b.id != bid]
    if len(new) == len(books):
        print("Book not found.")
    else:
        storage.save_books(new)
        print("Removed.")


def main_loop(path: str = None):
    storage = Storage(path)
    actions = {
        "1": ("List books", list_books),
        "2": ("Add book", add_book),
        "3": ("Search", search_books),
        "4": ("Borrow", borrow_book),
        "5": ("Return", return_book),
        "6": ("Remove book", remove_book),
        "0": ("Exit", None),
    }

    while True:
        print("\nLibrary Management")
        for k, (name, _) in actions.items():
            print(f"{k}. {name}")
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye.")
            break
        action = actions.get(choice)
        if not action:
            print("Invalid choice.")
            continue
        _, func = action
        func(storage)
