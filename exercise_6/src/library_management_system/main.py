from models import Library, Loan, Book, Member

if __name__ == "__main__":
    library = Library()

    books = [
        Book("978-1-23456-789-0", "Python Basics", "Alice Smith", 2020),
        Book("978-1-23456-789-1", "Advanced OOP", "Alice Smith", 2021),
        Book("978-1-23456-789-2", "Data Structures", "Bob Jones", 2019),
        Book("978-1-23456-789-3", "Algorithms", "Charlie Brown", 2022),
        Book("978-1-23456-789-4", "Web Development", "Dana White", 2023),
    ]

    for book in books:
        library.add_book(book)

    members = [
        Member("M001", "John"),
        Member("M002", "Mary"),
        Member("M003", "Paul"),
    ]

    for member in members:
        library.register_member(member)

    library.borrow_book(books[0], members[0])
    library.borrow_book(books[1], members[0])
    library.borrow_book(books[2], members[1])

    print()
    print("Search by title:", library.find_book_title("Python Basics"))
    print("Search by author:", library.find_book_author("Alice Smith"))
    print()

    try:
        library.borrow_book(books[0], members[0])
    except ValueError as exc:
        print("Duplicate borrow prevented:", exc)


    try:
        library.borrow_book(books[0], members[2])
    except ValueError as exc:
        print("Unavailable book prevented:", exc)
   
        
    member3 = members[2]
    for book in books[3:]:
        try:
            library.borrow_book(book, member3)
        except ValueError as exc:
            print("Member limit or duplicate prevented:", exc)
            break

    try:
        library.return_book(books[4], members[0])
    except ValueError as exc:
        print("Wrong member return prevented:", exc)
        print()

    library.return_book(books[0], members[0])
    print("Returned book status:", books[0].status_getter())

    try:
        library.return_book(books[0], members[0])
    except ValueError as exc:
        print("Returning an already returned book prevented:", exc)
        print()

    try:
        library.borrow_book(Book("999", "Bad Year", "X", 3000), members[0])
    except ValueError as exc:
        print("Invalid publication year prevented:", exc)

    try:
        library.borrow_book(books[4], Member("M999", "Ghost"))
    except ValueError as exc:
        print("Unregistered member prevented:", exc)