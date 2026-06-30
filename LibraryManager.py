import json
import os
from book import Book
from Member import Member
from BorrowRecord import BorrowRecord
from datetime import date, datetime

class LibraryManager:

    def __init__(self):
        self.books = []
        self.members = []
        self.books_borrowed = []
        self.BOOKS_FILENAME = "books.json"
        self.MEMBERS_FILENAME = "members.json"
        self.BORROW_RECORDS_FILENAME = "borrow_records.json"

    # Book related operations:
        
    def add_book(self, book_title: str, book_author: str, book_genre: str, book_publication_year: str):
        """Processes Book Insertion. Return True if successful, false if duplicate."""

        for book in self.books:
            if book.book_title.lower() == book_title.lower():
                return False
        
        new_book = Book(book_title, book_author, book_genre, book_publication_year)
        self.books.append(new_book)
        return True

    def view_books(self):
        """Display all books and their details available"""
        return sorted(self.books, key=lambda book:book.book_title.lower())
    
    def search_book(self, book_id: str = None, book_title: str= None):
        """Searches Book data based on provided Title of book or ID of the Book"""
        for book in self.books:
            if book_id and book.book_id.lower() == book_id.lower():
                return book
            if book_title and book.book_title.lower() == book_title.lower():
                return book
        return None
    
    def update_book(self, book_id: str, new_book_title: str = None, new_book_author: str = None, new_book_genre: str = None, new_book_publication_year: int = None):
        searched_book = self.search_book(book_id)
        if searched_book:
            if new_book_title:
                searched_book.book_title = new_book_title
            if new_book_author:
                searched_book.book_author = new_book_author
            if new_book_genre:
                searched_book.book_genre = new_book_genre
            if new_book_publication_year:
                searched_book.book_publication_year = new_book_publication_year
            return True
        return False
    
    def delete_book(self, book_id: str):
        book = self.search_book(book_id=book_id)
        if not book:
            return False
        # Check if currently borrowed (return_date is None = still out)
        for record in self.books_borrowed:
            if record.book_id == book_id and not record.is_returned():
                return "borrowed"
        self.books.remove(book)
        return True
    
    # Member related operations

    def add_member(self, member_name: str, member_age: int, member_phone: str):

        # Duplicate member check
        for member in self.members:
            if member.member_name.lower() == member_name.lower():
                return False
        
        new_member = Member(member_name, member_age, member_phone)
        self.members.append(new_member)
        return True
    
    def view_members(self):
        return sorted(self.members, key=lambda m:m.member_name.lower())
    
    def search_member(self, member_id: str=None, member_name: str = None):    
        for member in self.members:
            if member_id and member.member_id.lower() == member_id.lower():
                return member
            if member_name and member.member_name.lower() == member_name.lower():
                return member
        return None
    
    def update_member(self, member_id: str=None, member_name: str=None, new_member_name: str = None, new_member_age: int = None, new_member_phone: str = None):
        member = self.search_member(member_id, member_name)
        if member:
            if new_member_name:
                member.member_name = new_member_name
            if new_member_age:
                member.member_age = new_member_age
            if new_member_phone:
                member.member_phone = new_member_phone
            return True
        return False
        
    def delete_member(self, member_id: str=None, member_name:str=None):
        member = self.search_member(member_id, member_name)

        if not member:
            return False
        
        for record in self.books_borrowed:
            if record.member_id == member.member_id and not record.is_returned():
                return "has_books"
        self.members.remove(member)
        return True
    
    # Borrow book flow

    def borrow_book(self, book_id: str, member_id: str, borrow_date: date = None, return_date: date = None):
        member = self.search_member(member_id)
        book = self.search_book(book_id)

        if member and book:
            if book.book_available == True:
                book_borrowed = BorrowRecord(borrow_date=borrow_date, book_id=book_id, member_id=member_id)
                self.books_borrowed.append(book_borrowed)
                book.book_available = False
                return True
        return False

    def return_book(self, borrow_id: str):
        for book_borrow in self.books_borrowed:
            if book_borrow.borrow_id == borrow_id:
                if book_borrow.is_returned():
                    return "Already returned"
                book_borrow.return_date = date.today()
                book = self.search_book(book_borrow.book_id)
                book.book_available = True
                return True
        return False
    
    def display_borrowed_books(self):
        """Returns borrowing report data by joining records with book and member details."""
        if not self.books_borrowed:
            return None
        
        report = []
        for record in self.books_borrowed:
            book = self.search_book(record.book_id)
            member = self.search_member(record.member_id)
            
            report.append({
                "borrow_id": record.borrow_id,
                "book_title": book.book_title if book else "Unknown book",
                "member_name": member.member_name if member else "Unknown Member",
                "borrow_date": record.borrow_date.strftime("%d-%m-%Y"),
                "return_date": record.return_date.strftime("%d-%m-%Y") if record.return_date else "Not returned yet"
            })
        return report
    
    def save_data(self):
        """Saves all books, members, and borrow records to their JSON files."""
        data_mapping = {
            self.BOOKS_FILENAME: self.books,
            self.MEMBERS_FILENAME: self.members,
            self.BORROW_RECORDS_FILENAME: self.books_borrowed
        }

        try:
            for filename, list_data in data_mapping.items():
                with open(filename, 'w', encoding='utf-8') as json_file:
                    json.dump([item.to_dict() for item in list_data], json_file, indent=4)
            print("\n[System] Data saved successfully to file.")
        except Exception as e:
            print(f"\n[System] Error saving data: {e}")

    def load_data(self):
        """Loads books, members and borrow records from their json files on start"""    

        file_mapping = [
            (self.BOOKS_FILENAME, Book, self.books),
            (self.MEMBERS_FILENAME, Member, self.members),
            (self.BORROW_RECORDS_FILENAME, BorrowRecord, self.books_borrowed)
        ]

        any_loaded = False
        for filename, cls, target_lists in file_mapping:
            if not os.path.exists(filename):
                continue
            try:
                with open(filename, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                for d in data:
                    target_lists.append(cls.from_dict(d))
                any_loaded = True
            except Exception as e:
                print(f"\n[System] Error loading {filename}: {e}")

        if any_loaded:
            print("\n[System] Data loaded successfully from disk.")
        else:
            print("\n[System] No previous database found. Starting fresh.")
