import uuid
from datetime import datetime, date

class BorrowRecord():
    
    def __init__(self, borrow_date: date, return_date: date = None, borrow_id: str = None, book_id: str =  None, member_id: str = None):
        self.borrow_id = borrow_id if borrow_id else str(uuid.uuid4())
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date if borrow_date else date.today()
        self.return_date = return_date
    
    def __str__(self):
        date_str = self.return_date.strftime("%d-%m-%Y") if self.return_date else "Not returned yet"
        return (f"Borrow ID: {self.borrow_id} | Book ID: {self.book_id} | Member ID: {self.member_id} | Borrowed: {self.borrow_date} | Returned: {date_str}")
    
    def display_record(self):
        print(self)

    def is_returned(self):
        return self.return_date is not None
    
    def to_dict(self):
        return {
            "borrow_id": self.borrow_id,
            "book_id": self.book_id,
            "member_id": self.member_id,
            "borrow_date": self.borrow_date.strftime("%d-%m-%Y"),
            "return_date": self.return_date.strftime("%d-%m-%Y") if self.return_date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        borrow_date = datetime.strptime(data["borrow_date"], "%d-%m-%Y").date()
        return_date = datetime.strptime(data["return_date"], "%d-%m-%Y").date() if data["return_date"] else None
        return cls(borrow_date=borrow_date, return_date=return_date, borrow_id=data["borrow_id"], book_id=data["book_id"], member_id=data["member_id"])
