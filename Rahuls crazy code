# ==============================
# Library Management System
# Basic Python Version
# ==============================

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

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    }

    books.append(book)
    print("Book added successfully!")

def view_books():
    print("\n--- Available Books ---")
    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | "
              f"Author: {book['author']} | Qty: {book['quantity']}")

def search_book():
    keyword = input("Enter book title or author: ").lower()
    found = False

    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(book)
            found = True

    if not found:
        print("Book not found.")

# ------------------------------
# User Functions
# ------------------------------
def add_user():
    print("\n--- Add User ---")
    user_id = input("User ID: ")
    name = input("Name: ")
    role = input("Role (admin/librarian/member): ").lower()

    user = {
        "id": user_id,
        "name": name,
        "role": role
    }

    users.append(user)
    print("User added successfully!")

def view_users():
    print("\n--- Registered Users ---")
    for user in users:
        print(f"ID: {user['id']} | Name: {user['name']} | Role: {user['role']}")

# ------------------------------
# Issue & Return Functions
# ------------------------------
def issue_book():
    print("\n--- Issue Book ---")
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
    print("\n--- Return Book ---")
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
# Interfaces
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
            print(f"Welcome {user['name']}!")

            if user["role"] == "admin":
                admin_menu()
            elif user["role"] == "librarian":
                librarian_menu()
            elif user["role"] == "member":
                member_menu()
            return

    print("User not found.")

# ------------------------------
# Main Program
# ------------------------------
def main():
    # Default Admin
    users.append({"id": "admin", "name": "System Admin", "role": "admin"})

    while True:
        clear()
        print("=== Library Management System ===")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            pause()

# Run Program
main(
