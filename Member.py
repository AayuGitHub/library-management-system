import uuid

class Member:
    def __init__(self, member_name: str, member_age: int, member_phone: str, member_id: str = None):
        self.member_id = member_id if member_id else str(uuid.uuid4())
        self.member_name = member_name
        self.member_age = member_age
        self.member_phone = member_phone

    def __str__(self):
        """Function to display Member details in string format"""
        return f"\nMember ID: {self.member_id} | Member Name: {self.member_name} | Member age: {self.member_age} | Member Phone: {self.member_phone}"
    
    def display_member(self):
        """Display Member Details in formatted way"""
        print(self)
    
    def to_dict(self):
        """Converts object data back to a dictionary layout for easy JSON saving"""
        return {
            "member_id": self.member_id,
            "member_name": self.member_name,
            "member_age": self.member_age,
            "member_phone": self.member_phone
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["member_name"], data["member_age"], data["member_phone"], data["member_id"] )