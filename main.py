from book import Book
from Member import Member
from LibraryManager import LibraryManager

libraryManager = LibraryManager()

libraryManager.load_data()

while True:

    print("\n===============================\n")
    print("Main Menu\n")
    print("===============================\n")
    print("    1.  Add Book\n")
    print("    2.  View Books\n")
    print("    3.  Search Book\n")
    print("    4.  Update Book\n")
    print("    5.  Delete Book\n\n")
    print("    6.  Add Member\n")
    print("    7.  View Member\n")
    print("    8.  Search Member\n")
    print("    9.  Update Member\n")
    print("    10. Delete Member\n")
    print("    11.  Borrow Book\n")
    print("    12.  Return Book\n")
    print("    13.  Borrowing Report\n")
    print("    14.  Exit\n")

    choice = input("Please select (1-14): ")

    if choice == "1":
        book_title = input("Please enter the title of the book: ").strip()
        while book_title == "":
            book_title = input("Title of the book can't be empty; please enter the title:  ").strip()
        
        book_author = input("Please enter the author of the book: ").strip()
        while book_author == "":
            book_author = input("Author of the book can't be empty; please enter the author:  ").strip()
        
        book_genre = input("Please enter the genre of the book: ").strip()
        while book_genre == "":
            book_genre = input("Genre of the book can't be empty; please enter the genre:  ").strip()

        book_publication_year = input("Please enter the year of the book when it's published: ")
        while book_publication_year == "":
            book_publication_year = input("Please enter the year of the book when it's published: ").strip()
        book_year = int(book_publication_year)

        new_book = libraryManager.add_book(book_title, book_author, book_genre, book_year)
        if new_book:
            print("\nBook added successfully!")
        else:
            print("\nBook already exists! Please add new book!")

    elif choice == "2":
        print("\nDisplaying all books and their details: \n") 
        books = libraryManager.view_books()
        for book in books:
            print("\n---------------------------------")
            print(f"\nBook ID: {book.book_id}")
            print(f"\nBook Title: {book.book_title}")
            print(f"\nBook Author: {book.book_author}")
            print(f"\nBook Genre: {book.book_genre}")
            print(f"\nBook Published Year: {book.book_publication_year}")
            print(f"\nBook Status: {book.book_available}")
            print("\n---------------------------------")

    elif choice == "3":
        print("\nDisplaying all books and their details for you to select ID and title which you want to search for: ") 

        books = libraryManager.view_books()
        for book in books:
            print(f"\nBook ID: {book.book_id} | Book Title: {book.book_title} | Book Author: {book.book_author} | Book Genre: {book.book_genre} | Book Published Year: {book.book_publication_year} | Book Status: {book.book_available}\n")
        
        input_book_id = input("\nEnter the ID of the book which you want to search: ").strip()

        input_book_title = input("\nEnter the title of the book which you want to search: ").strip()

        searched_book = libraryManager.search_book(input_book_id, input_book_title)

        if searched_book:
            print("\n---------------------------------")
            print(f"\nBook ID: {searched_book.book_id}")
            print(f"\nBook Title: {searched_book.book_title}")
            print(f"\nBook Author: {searched_book.book_author}")
            print(f"\nBook Genre: {searched_book.book_genre}")
            print(f"\nBook Published Year: {searched_book.book_publication_year}")
            print(f"\nBook Status: {searched_book.book_available}")
            print("\n---------------------------------")
        else:
            print("\nSearched book doesn't exist in dB. Please add it using option 1.")

    elif choice == "4":
        print("\nDisplaying all books and their details for you to select ID and title which you want to update: \n") 

        books = libraryManager.view_books()
        for book in books:
            print(f"\nBook ID: {book.book_id} | Book Title: {book.book_title} | Book Author: {book.book_author} | Book Genre: {book.book_genre} | Book Published Year: {book.book_publication_year} | Book Status: {book.book_available}\n")

        input_book_id = input("\nEnter the book Id which you want to update: ")
        while input_book_id == "":
            input_book_id = input("\nBook ID can't be empty; please enter the book Id which you want to update").strip()
        
        new_book_title = input(f"Please enter the new title of the book {input_book_id} (Keep blank to skip it): ")
        
        new_book_author = input(f"Please enter the new author of the book {input_book_id} (Keep blank to skip it)")
        
        new_book_genre = input(f"Please enter the new genre of the book {input_book_id} (Keep blank to skip it)")
        
        new_book_publication_year = input(f"Please enter the new publication year of the book {input_book_id} (Keep blank to skip it): ")

        new_book_publication_year_int = int(new_book_publication_year) if new_book_publication_year.strip() != "" else None

        update_book = libraryManager.update_book(input_book_id, new_book_title, new_book_author, new_book_genre, new_book_publication_year_int)

        if update_book:
            print(f"\n Book with {input_book_id} has been updated successfully!")
        else:
            print(f"\nBook with {input_book_id} doesn't exist, please add first using option 1")
        
    elif choice == "5":
        print("\nDisplaying all books and their details for you to select ID which you want to delete: \n") 

        books = libraryManager.view_books()
        for book in books:
            print(f"\nBook ID: {book.book_id} | Book Title: {book.book_title} | Book Author: {book.book_author} | Book Genre: {book.book_genre} | Book Published Year: {book.book_publication_year} | Book Status: {book.book_available}\n")

        input_book_id = input("\nEnter the book Id which you want to delete: ").strip()
        while input_book_id == "":
            input_book_id = input("\nBook ID can't be empty; please enter the book Id which you want to delete").strip()

        result = libraryManager.delete_book(input_book_id)
        if result == True:
            print(f"\nBook deleted successfully!")
        elif result == "borrowed":
            print("\nBook cannot be deleted because it is currently issued.")
        else:
            print(f"\nBook doesn't exist.")

    elif choice == "6":
        print("\nPlease add below details of member to add a member: ")
        
        member_name = input("\nPlease add member name here: ").strip()
        while member_name == "":
            member_name = input("\nPlease add member name here: ").strip()
        
        while True:
            try:
                member_age = int(input("Enter the age of member: "))
                break
            except ValueError:
                print("Invalid Input! Age must be a whole number. Please try again.")
        
        member_phone = input("\nPlease add phone number (10-digit) of member: ")
        while member_phone == "":
            member_phone = input("\nPlease add phone number (10-digit) of member: ")

        new_member = libraryManager.add_member(member_name, member_age, member_phone)

        if new_member:
            print(f"\nNew member ({member_name}) has been added successfully!")
        else:
            print("New member couldn't be added, please try adding again!")
        
    elif choice == "7":
        members = libraryManager.view_members()
        if members:
            for member in members:
                print("\n---------------------------------")
                print(f"\nMember ID: {member.member_id}")
                print(f"\nMember Name: {member.member_name}")
                print(f"\nMember Age: {member.member_age}")
                print(f"\nMember Phone: {member.member_phone}")
                print("\n---------------------------------")
        else:
            print("\nNo History in Members Db. Please add Members using option 6.")

    elif choice == "8":
        print("\nDisplaying members and their details for you to select Member ID and name for you to search member: ")
        members = libraryManager.view_members()
        if members:
            for member in members:
                print(f"\nMember ID: {member.member_id} | Member Name: {member.member_name} | Member Age: {member.member_age} | Member Phone: {member.member_phone}")
        else:
            print("\nNo History in Members Db. Please add Members using option 6.")

        input_member_id = input("\nPlease add Member ID for which you want to search: ")

        input_member_name = input("\nPlease add Member name for which you want to search: ")

        search_member = libraryManager.search_member(input_member_id, input_member_name)

        if search_member is None:
            print(f"\nMember with ({input_member_id}) couldn't be found, please add them using option 6!")
        else:
            print("\n---------------------------------")
            print(f"\nMember ID: {search_member.member_id}")
            print(f"\nMember Name: {search_member.member_name}")
            print(f"\nMember Age: {search_member.member_age}")
            print(f"\nMember Phone: {search_member.member_phone}")
            print("\n---------------------------------")
    
    elif choice == "9":
        print("\nDisplaying members and their details for you to select Member ID and name for you to update member: ")
        members = libraryManager.view_members()
        if members:
            for member in members:
                print(f"\nMember ID: {member.member_id} | Member Name: {member.member_name} | Member Age: {member.member_age} | Member Phone: {member.member_phone}")
        else:
            print("\nNo History in Members Db. Please add Members using option 6.")
        
        input_member_id = input("\nPlease add Member ID for which you want to update: ")
        
        input_member_name = input("\nPlease add Member name for which you want to update: ")

        new_member_name = input(f"\nEnter the new member name for member ({input_member_id}) (Keep it blank to skip it): ").strip()

        new_member_age = None
        age_str = input(f"Enter new age (leave blank to skip): ").strip()
        if age_str != "":
            while True:
                try:
                    new_member_age = int(age_str)
                    break
                except ValueError:
                    age_str = input("Age must be a whole number: ").strip()


        new_member_phone = input(f"\nEnter the new phone number of member for member ({input_member_id}) (Keep it blank to skip it): ").strip()

        update_member = libraryManager.update_member(input_member_id, input_member_name, new_member_name, new_member_age, new_member_phone)

        if update_member:
            print(f"\nMember with {input_member_id} is updated successfully!")
        else:
            print(f"\nMember with {input_member_id} doesn't exist in DB!")

    elif choice == "10":
        print("\nDisplaying members and their details for you to select Member ID and name for you to delete member: ")
        members = libraryManager.view_members()
        if members:
            for member in members:
                print(f"\nMember ID: {member.member_id} | Member Name: {member.member_name} | Member Age: {member.member_age} | Member Phone: {member.member_phone}")
        else:
            print("\nNo History in Members Db. Please add Members using option 6.")
        
        input_member_id = input("\nPlease add Member ID for which you want to delete: ")

        input_member_name = input("\nPlease add Member name for which you want to delete")

        result = libraryManager.delete_member(input_member_id, input_member_name)
        if result == True:
            print(f"\nMember deleted successfully!")
        elif result == "has_books":
            print("\nMember still has borrowed books. Cannot delete.")
        else:
            print(f"\nMember doesn't exist.")
        
    elif choice == "11":
        print("\nDisplaying all books and their details for you to select ID and title which you want to search for: \n") 

        books = libraryManager.view_books()
        for book in books:
            print(f"\nBook ID: {book.book_id} : Book Title: {book.book_title}\n")

        print("\nDisplaying members and their details for you to select Member ID and name for you to  : ")
        members = libraryManager.view_members()
        if members:
            for member in members:
                print(f"\nMember ID: {member.member_id} : Member Name: {member.member_name}")
        else:
            print("\nNo History in Members Db. Please add Members using option 6.")

        print("\nPlease fill below details to borrow the book: ")
        
        input_book_id = input("Enter the Book ID which you want to borrow: ").strip()
        while input_book_id == "":
            input_book_id = input("Book ID can't be empty; enter the Book ID which you want to borrow: ").strip() 

        input_member_id = input("Enter the Member ID of yours: ")
        while input_member_id == "":
            input_member_id = input("Member ID can't be empty; enter the Member ID of yours: ").strip()

        borrow_book = libraryManager.borrow_book(input_book_id, input_member_id)

        if borrow_book:
            print(f"\nBook ({input_book_id}) borrowed successfully by member ({input_member_id})!")
        else:
            print(f"\nCouldn't borrow — either the Member ID or Book ID doesn't exist, or the book is already borrowed.")

    elif choice == "12":
        input_borrow_id = input("\nPlease enter Borrow ID to return the book you borrowed: ")

        return_book = libraryManager.return_book(input_borrow_id)

        if return_book:
            print(f"\nYou've returned the book with borrow ID being ({input_borrow_id})")
        else:
            print(f"\nYou've not borrowed any book yet; please borrow the book first using option 11.")

    elif choice == "13":
        borrowed_book_records = libraryManager.display_borrowed_books()

        if borrowed_book_records is None:
            print("\nNo record of Borrowed books exist yet; please borrow books first.")
        else:
            for item in borrowed_book_records:
                print("\n---------------------------------")
                print(f"\nBorrow ID: {item["borrow_id"]}")
                print(f"\nBook Title: {item["book_title"]}")
                print(f"\nMember Name: {item["member_name"]}")
                print(f"\nBorrow Date: {item["borrow_date"]}")
                print(f"\nReturn Date: {item["return_date"]}")
                print("\n---------------------------------")
    
    elif choice == "14":
        print("\nSaving Data...!")
        libraryManager.save_data()
        print("\n Exiting. Good bye")
        break
    else:
        print("\nInvalid Option added! Please enter option from 1-14!")
        















            

    
