# ==================================
# Library Management System
# Prepared & Preloaded Version
# ==================================

# ------------------------------
# Global Data Storage
# ------------------------------
books = []
users = []
issued_books = []

# ------------------------------
# Utility Functions
# ------------------------------
def pause():
    input("\nPress Enter to continue...")

def clear():
    print("\n" * 3)

# ------------------------------
# Book Functions
# ------------------------------
def add_book():
    print("\n--- Add Book ---")
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    quantity = int(input("Quantity: "))

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    })

    print("Book added successfully!")

def view_books():
    print("\n--- Available Books ---")
    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        print(f"ID: {book['id']} | "
              f"Title: {book['title']} | "
              f"Author: {book['author']} | "
              f"Qty: {book['quantity']}")

def search_book():
    keyword = input("Enter title or author: ").lower()
    found = False

    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(book)
            found = True

    if not found:
        print("No matching book found.")

# ------------------------------
# User Functions
# ------------------------------
def add_user():
    print("\n--- Add User ---")
    user_id = input("User ID: ")
    name = input("Name: ")
    role = input("Role (admin/librarian/member): ").lower()

    users.append({
        "id": user_id,
        "name": name,
        "role": role
    })

    print("User added successfully!")

def view_users():
    print("\n--- Registered Users ---")
    for user in users:
        print(f"ID: {user['id']} | "
              f"Name: {user['name']} | "
              f"Role: {user['role']}")

# ------------------------------
# Issue & Return Functions
# ------------------------------
def issue_book():
    user_id = input("User ID: ")
    book_id = input("Book ID: ")

    for book in books:
        if book["id"] == book_id and book["quantity"] > 0:
            book["quantity"] -= 1
            issued_books.append({
                "user_id": user_id,
                "book_id": book_id
            })
            print("Book issued successfully!")
            return

    print("Book not available.")

def return_book():
    user_id = input("User ID: ")
    book_id = input("Book ID: ")

    for record in issued_books:
        if record["user_id"] == user_id and record["book_id"] == book_id:
            issued_books.remove(record)

            for book in books:
                if book["id"] == book_id:
                    book["quantity"] += 1
                    print("Book returned successfully!")
                    return

    print("Issue record not found.")

# ------------------------------
# Menus
# ------------------------------
def admin_menu():
    while True:
        clear()
        print("=== Admin Menu ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add User")
        print("4. View Users")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            add_user()
        elif choice == "4":
            view_users()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

        pause()

def librarian_menu():
    while True:
        clear()
        print("=== Librarian Menu ===")
        print("1. View Books")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

        pause()

def member_menu():
    while True:
        clear()
        print("=== Member Menu ===")
        print("1. View Books")
        print("2. Search Book")
        print("3. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

        pause()

# ------------------------------
# Login System
# ------------------------------
def login():
    user_id = input("Enter User ID: ")

    for user in users:
        if user["id"] == user_id:
            print(f"Welcome, {user['name']}!")

            if user["role"] == "admin":
                admin_menu()
            elif user["role"] == "librarian":
                librarian_menu()
            elif user["role"] == "member":
                member_menu()
            return

    print("User not found.")
    pause()

# ------------------------------
# Preloaded Data
# ------------------------------
def load_data():
    # Users
    users.extend([
        {"id": "admin1", "name": "Alice", "role": "admin"},
        {"id": "lib1", "name": "Bob", "role": "librarian"},
        {"id": "lib2", "name": "Carol", "role": "librarian"},
        {"id": "mem1", "name": "David", "role": "member"},
        {"id": "mem2", "name": "Eva", "role": "member"}
    ])

    # Books
    books.extend([
        {"id": "B101", "title": "Python Basics", "author": "Guido", "quantity": 5},
        {"id": "B102", "title": "Data Structures", "author": "Mark Allen", "quantity": 3},
        {"id": "B103", "title": "Operating Systems", "author": "Andrew Tanenbaum", "quantity": 4},
        {"id": "B104", "title": "Computer Networks", "author": "Forouzan", "quantity": 2}
    ])

# ------------------------------
# Main Program
# ------------------------------
def main():
    load_data()

    while True:
        clear()
        print("=== Library Management System ===")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice.")
            pause()

# Run Program
main()
