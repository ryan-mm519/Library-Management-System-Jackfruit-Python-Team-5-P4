# ---------------- LIBRARY SYSTEM (CLOSURE) ---------------- #

def create_library():
    books, users, bid = {}, {}, 1

    def add_book(t, a, y, c):
        nonlocal bid
        books[bid] = [t, a, y, c, c]
        bid += 1
        return f"Book added with ID {bid-1}"

    def remove_book(b):
        return "Book removed" if books.pop(b, None) else "Invalid book ID"

    def view_all_books():
        return books

    def register_user(u):
        users.setdefault(u, set())
        return "User ready"

    def borrow_book(u, b):
        if u not in users or b not in books or books[b][4] < 1:
            return "Cannot borrow"
        users[u].add(b)
        books[b][4] -= 1
        return "Book borrowed"

    def return_book(u, b):
        if b not in users.get(u, []):
            return "Cannot return"
        users[u].remove(b)
        books[b][4] += 1
        return "Book returned"

    def search_books(k):
        k = k.lower()
        return [(i, *v) for i, v in books.items()
                if k in v[0].lower() or k in v[1].lower()]

    def view_available_books():
        return [(i, *v) for i, v in books.items() if v[4] > 0]

    return locals()


# ---------------- ADMIN MENU ---------------- #

def admin_menu(lib):
    while True:
        print("1. Add Book\n2. Remove Book\n3. View Books\n4. Back")

        c = input("Choice: ")

        if c == "1":
            print(lib["add_book"](
                input("Title: "), input("Author: "),
                input("Year: "), int(input("Copies: "))
            ))
        elif c == "2":
            print(lib["remove_book"](int(input("Book ID: "))))
        elif c == "3":
            for i, b in lib["view_all_books"]().items():
                print(i, "|", b[0], "by", b[1], "| Available:", b[4])
        elif c == "4":
            break
        else:
            print("Invalid choice")


# ---------------- CUSTOMER MENU ---------------- #

def customer_menu(lib):
    user = input("Username: ")
    lib["register_user"](user)

    while True:
        print("\n1.Search  2.Borrow  3.Return  4.Available  5.Back")
        c = input("Choice: ")

        if c == "1":
            for r in lib["search_books"](input("Keyword: ")):
                print(r)
        elif c == "2":
            print(lib["borrow_book"](user, int(input("Book ID: "))))
        elif c == "3":
            print(lib["return_book"](user, int(input("Book ID: "))))
        elif c == "4":
            for b in lib["view_available_books"]():
                print(b)
        elif c == "5":
            break
        else:
            print("Invalid choice")


# ---------------- MAIN PROGRAM ---------------- #

def main():
    lib = create_library()

    while True:
        print("\n1.Admin  \n2.Customer  \n3.Exit")
        c = input("Choice: ")

        if c == "1":
            admin_menu(lib)
        elif c == "2":
            customer_menu(lib)
        elif c == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()
