# Library Management System

A command-line application for a local library to replace paper records — manage books, register members, borrow and return books, and generate reports, with all data saved automatically across sessions.

Built with Python as a learning project to move beyond single-object management and practice how multiple object types relate to and interact with each other.

---

## What it does

You get a menu with 14 options when you run the app:

```
===============================
 Library Management System
===============================

    1.  Add Book          6.  Add Member
    2.  View Books        7.  View Members
    3.  Search Book       8.  Search Member
    4.  Update Book       9.  Update Member
    5.  Delete Book       10. Delete Member

    11. Borrow Book
    12. Return Book

    13. Borrowing Report

    14. Exit
```

Books, members, and borrow records are saved to three separate JSON files on exit and loaded back automatically on the next run.

---

## How to run it

You just need Python 3 — no external libraries required.

```bash
python3 main.py
```

---

## Project structure

```
Library_Management_System/
├── main.py               # Entry point — menu loop and all user input/output
├── book.py               # Book class — represents one book in the library
├── Member.py             # Member class — represents one registered member
├── BorrowRecord.py       # BorrowRecord class — represents one borrow transaction
├── LibraryManager.py     # All business logic — owns all three collections
├── books.json            # Auto-created on first save
├── members.json          # Auto-created on first save
└── borrow_records.json   # Auto-created on first save
```

### How the files relate to each other

- **`book.py`** is the blueprint for a single book — title, author, genre, year, and availability status. When a book is borrowed, the manager flips `book_available` to `False`.
- **`Member.py`** is the blueprint for a registered member — name, age, and phone number.
- **`BorrowRecord.py`** is the blueprint for a single borrowing transaction. It stores the book's ID and the member's ID — not the full objects. The borrow date is set automatically to today; the return date starts as `None` and gets filled when the book is returned.
- **`LibraryManager.py`** owns all three lists and handles every operation — adds, searches, updates, deletes, borrow/return logic, report generation, and JSON persistence. It's the only file that knows about all three data types.
- **`main.py`** never touches data directly. It asks the user for input, calls a method on `LibraryManager`, and prints the result.

---

## Features

- **Add a book** — Enter title, author, genre, and publication year. Book ID is generated automatically.
- **View all books** — Lists every book alphabetically, showing ID, title, author, genre, year, and availability.
- **Search a book** — Find by Book ID or title. Either one works independently.
- **Update a book** — Change any combination of title, author, genre, or year. Leave a field blank to skip it.
- **Delete a book** — Only allowed if the book is not currently borrowed. Blocked with a clear message if it's issued.
- **Add a member** — Enter name, age, and phone. Member ID is generated automatically.
- **View all members** — Lists every registered member alphabetically.
- **Search a member** — Find by Member ID or name.
- **Update a member** — Change name, age, or phone. Blank fields are skipped.
- **Delete a member** — Only allowed if the member has no unreturned books.
- **Borrow a book** — Enter Member ID and Book ID. The system checks both exist and the book is available before creating a borrow record and marking the book unavailable.
- **Return a book** — Enter the Borrow ID. The system records today's date as the return date and marks the book available again.
- **Borrowing report** — Shows all borrow records with book title, member name, borrow date, and return status — pulling names from the related Book and Member objects by ID.
- **Persistent storage** — All three JSON files are written on exit and read on startup. UUIDs and dates are fully preserved across sessions.

---

## What I learned building this

- How to model **relationships between objects** — a `BorrowRecord` doesn't own a Book or Member, it just stores their IDs and looks them up when needed. This is composition, not inheritance.
- Why **inheritance is the wrong tool** for a borrow record — `class BorrowRecord(Book, Member)` would mean "a borrow record IS a book AND a member," which makes no sense. It should just reference them by ID.
- The **"join" pattern** — to build the borrowing report, you loop through records, look up the book by `book_id` and the member by `member_id`, then combine fields from all three objects into one display. The same concept as a database JOIN.
- How returning **different values from one function** (`True` / `False` / `"borrowed"` / `"has_books"`) lets the caller show the right message for each outcome — not just success or failure, but *why* it failed.
- The difference between `is not None` and truthiness — `if value is not None` lets empty strings through and overwrites data with blanks. `if value:` skips both `None` and `""`, which is what you actually want for optional update fields.
- That **`print()` returns `None`** — using `print()` where you meant `input()` assigns `None` to the variable, and any method call on it immediately crashes.
- The **trailing comma tuple trap** — `self.name = name,` stores `("Aayush",)` instead of `"Aayush"`. Python silently treats a lone trailing comma as a tuple, not a value.
- The **`&` vs `and` operator** — `member & book` tries bitwise AND on two objects and crashes. `member and book` checks if both are truthy, which is what you want.
- How to use the same **save and load mapping pattern** for multiple files — pairing `(filename, class, list)` in a tuple lets one loop handle all three collections without repeating yourself.
- Why **`borrow_date` defaults to `date.today()`** inside the constructor — the caller shouldn't have to pass the current date every time. The object should handle its own sensible defaults.
