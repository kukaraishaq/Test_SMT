import math

# Inventory
inventory = []

# Inventory functions
def add_book(title):
    inventory.append({"title": title, "borrowed": False})

def remove_book(title):
    global inventory
    inventory = [book for book in inventory if book["title"] != title]

def display_inventory():
    for book in inventory:
        status = "Borrowed" if book["borrowed"] else "Available"
        print(f"{book['title']} - {status}")

# Borrow/Return functions
def borrow_book(title):
    for book in inventory:
        if book["title"] == title and not book["borrowed"]:
            book["borrowed"] = True
            print(f"You borrowed '{title}'")
            return
    print(f"'{title}' is not available.")

def return_book(title, days_late=0):
    for book in inventory:
        if book["title"] == title and book["borrowed"]:
            book["borrowed"] = False
            fine = math.ceil(days_late * 0.5)
            print(f"'{title}' returned. Fine: ${fine}")
            return
    print(f"'{title}' was not borrowed.")

def check_availability(title):
    for book in inventory:
        if book["title"] == title:
            return not book["borrowed"]
    return False

# Demo
add_book("Python 101")
add_book("Data Science Handbook")
display_inventory()

borrow_book("Python 101")
display_inventory()
return_book("Python 101", days_late=3)
display_inventory()

# Lambda: filter borrowed books
overdue_books = list(filter(lambda b: b["borrowed"], inventory))
print("Overdue books:", [b["title"] for b in overdue_books])

# List comprehension: borrowed books report
borrowed_report = [b["title"] for b in inventory if b["borrowed"]]
print("Borrowed books report:", borrowed_report)
