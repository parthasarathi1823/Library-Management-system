import logging
logger=logging.getLogger(__name__)

file_handler=logging.FileHandler("logfiles.log")

logger.addHandler(file_handler)

formatter=logging.Formatter("%(levelname)s:%(asctime)s:%(message)s")

file_handler.setFormatter(formatter)

logger.setLevel(logging.INFO)

class Book:
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn  # ISBN is a unique number for each book
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print("\nBook Borrowed Successfully...\n")
        else:
            print("\nBook Not Available\n")

    def return_book(self):
        if not self.available:
            self.available = True
            print("\nBook Returned Successfully...\n")
        else:
            print("\nYou can't return it!\n")

    

class Library:
    def __init__(self):
        self.books = {}

    def validate_book(self, isbn):
        return self.books.get(isbn)

    def add_book(self, name, author, isbn):
        if isbn in self.books:
            print("\nBook already available\n")
        else:
            self.books[isbn] = Book(name, author, isbn)
            print("\nBook added successfully\n")

    def borrow_book(self, isbn):
        book = self.validate_book(isbn)
        if book:
            book.borrow_book()
        else:
            print("\nBook not found\n")

    def return_book(self, isbn):
        book = self.validate_book(isbn)
        if book:
            book.return_book()
        else:
            print("\nBook not found\n")

    def display_book(self, isbn):
        book = self.validate_book(isbn)
        if book:
            book.display_book()
        else:
            print("\nBook not found\n")

    def disp_lib(self):
        if not self.books:
            print("\nNo Books Available.\n")
            return

        print("\n==== List of Books in Library ====\n")
        for isbn, book in self.books.items():
            print(f"Book Name: {book.name} | ISBN: {isbn}\n")
            print("-" * 40 + "\n")
        print("\n")


# CLI Program
lib = Library()

print("================= Welcome to ABC Library ===================\n")

while True:
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display All Books")
    print("5. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nPlease enter a valid number!\n")
        continue

    if choice == 1:
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        try:
            isbn = int(input("Enter Book ISBN: "))
        except ValueError:
            print("\nISBN must be a number!\n")
            logger.error("Error While Adding New Book")
            continue
        lib.add_book(name, author, isbn)
        logger.info("New Book : Name={} Author={} ISBN={} Added".format(name,author,isbn))

    elif choice == 2:
        try:
            isbn = int(input("Enter ISBN to borrow: "))
        except ValueError:
            logger.error("Error in ISBN")
            print("\nISBN must be a number!\n")
            continue
        lib.borrow_book(isbn)
        logger.info("Book : ISBN={} Borrowed".format(isbn))

    elif choice == 3:
        try:
            isbn = int(input("Enter ISBN to return: "))
        except ValueError:
            print("\nISBN must be a number!\n")
            logger.error("Error in ISBN")
            continue
        lib.return_book(isbn)
        logger.info("Book : ISBN={} Returned".format(isbn))

    elif choice == 4:
        lib.disp_lib()
        logger.info("All Books Verified")

    elif choice == 5:
        print("\nThanks for Visiting ✨\n")
        break

    else:
        print("\nInvalid choice! Please try again.\n")
        logger.error("Invalid Attempt")
