from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Monthly", 2, 42)
dvd = DVD("Inception", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 0. Abstract class cannot be instantiated
print("=== 0. Abstract parent ===")
try:
    LibraryItem("x", 99)
except TypeError:
    print("TypeError: LibraryItem is abstract and cannot be created directly.")

# 1. Borrowing with error handling
print("\n=== 1. Borrowing ===")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Limit error and not-borrowed error
print("\n=== 2. More error handling ===")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.return_item(dvd)  # Alice never borrowed it
except ValueError as e:
    print("Could not return:", e)

fee = alice.return_item(book, days_late=3)
print(f"Alice returned '{book.title}'. Late fee: Rs {fee}")
print("Alice's items:", alice.borrowed_titles())
print("Bob's items:", bob.borrowed_titles())

# 3. Polymorphism: one loop, no type checks
print("\n=== 3. Polymorphism ===")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("\n=== 4. Class attribute ===")
print("Total items created:", LibraryItem.total_items)

# 5. Encapsulation
print("\n=== 5. Encapsulation ===")
try:
    print(book.__available)
except AttributeError as e:
    print("AttributeError:", e)
print("Via is_available():", book.is_available())
print("Magazine available?", magazine.is_available())