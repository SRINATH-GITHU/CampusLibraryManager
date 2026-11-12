# Library Manager

Run with `python3 main.py` (Python 3.12+, no external packages).

## Reflection

**1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**
LibraryItem is abstract because "a generic item" is not something the library
actually lends. It only exists to share common code and to force every real
item type to provide its own `late_fee()`. If DVD forgets `late_fee()`, Python
raises a TypeError as soon as you try to create a DVD object, so the mistake
is caught immediately instead of at fee-calculation time.

**2. What happens when you read item.__available from outside the class, and why do we use is_available()?**
It raises an AttributeError. Python renames private attributes inside the
class (name mangling, to `_LibraryItem__available`), so the plain name does
not exist from outside. We use `is_available()` so that only the class's own
methods change or expose the state. That keeps availability consistent and
lets us add rules later without breaking other code.

**3. What is the difference between LibraryItem.total_items and self.title?**
`total_items` is a class attribute: one value shared by every item, accessed
through the class, and incremented on each object creation. `self.title` is an
instance attribute: each object has its own copy, so a Book and a DVD can have
different titles.