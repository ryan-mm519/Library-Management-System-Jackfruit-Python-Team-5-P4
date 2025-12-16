books = {}
issued_books = {}

def add_book():
    bid = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    books[bid] = {"title": title, "author": author, "available": True}
    print("Book added successfully.\n")

def remove_book():
    bid = input("Enter Book ID to remove: ")
    if bid in books:
        del books[bid]
        print("Book removed.\n")
    else:
        print("Book not found.\n")

def search_book():
    key = input("Enter title or Book ID to search: ").lower()
    found = False
    for bid, info in books.items():
        if key in bid.lower() or key in info["title"].lower():
            print(bid, info)
            found = True
    if not found:
        print("No matching book found.\n")

def issue_book():
    usn = input("Enter Student USN: ")
    bid = input("Enter Book ID to issue: ")

    if bid not in books:
        print("Book not found.\n")
        return
    if not books[bid]["available"]:
        print("Book already issued.\n")
        return

    books[bid]["available"] = False
    issued_books.setdefault(usn, []).append(bid)
    print("Book issued successfully.\n")

def return_book():
    usn = input("Enter Student USN: ")
    bid = input("Enter Book ID to return: ")

    if usn in issued_books and bid in issued_books[usn]:
        issued_books[usn].remove(bid)
        books[bid]["available"] = True
        print("Book returned.\n")
    else:
        print("Invalid return.\n")

def display_books():
    for bid, info in books.items():
        print(bid, info)
    print()

def menu():
    while True:
        print("1 Add\n2 Remove\n3 Search\n4 Issue\n5 Return\n6 Display\n0 Exit")
        choice = input("Enter choice: ")
        print()

        if choice == "1": add_book()
        elif choice == "2": remove_book()
        elif choice == "3": search_book()
        elif choice == "4": issue_book()
        elif choice == "5": return_book()
        elif choice == "6": display_books()
        elif choice == "0": break
        else: print("Invalid choice\n")

menu()
