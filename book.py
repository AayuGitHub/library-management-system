import uuid

class Book:

    def __init__(self, book_title: str, book_author: str, book_genre: str, book_publication_year: int, book_available: bool=True, book_id: str = None):
        self.book_id = book_id if book_id else str(uuid.uuid4())
        self.book_title = book_title
        self.book_author = book_author
        self.book_genre = book_genre
        self.book_publication_year = book_publication_year
        self.book_available = book_available

    def __str__(self):
        """Controls how Book details look like when you print it"""
        return f"\nBook ID: {self.book_id} | Book Title: {self.book_title} | Book Author: {self.book_author} | Book Genre: {self.book_genre} | Book Publication year: {self.book_publication_year} | Book Available: {self.book_available}"

    def display_book(self):
        """Displays book details in formatted way"""
        print(self)

    def to_dict(self):
        """Converts book object back to dictionary"""
        return {
            "book_id": self.book_id,
            "book_title": self.book_title,
            "book_author": self.book_author,
            "book_genre": self.book_genre,
            "book_publication_year": self.book_publication_year,
            "book_available": self.book_available
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["book_title"], data["book_author"], data["book_genre"], data["book_publication_year"], data["book_available"], data["book_id"])