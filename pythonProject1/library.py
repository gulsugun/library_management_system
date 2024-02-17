class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def __del__(self):
        if self.file:
            self.file.close()

    def list_books(self):
        self.file.seek(0)
        contents = self.file.read()
        lines = contents.splitlines()
        for line in lines:
            book_info = line.split(',')
            if len(book_info) == 4:
                book_title, author, release_year, num_pages = book_info
                print(f"Book: {book_title.strip()}, Author: {author.strip()}, Release Year: {release_year.strip()}, Number of Pages: {num_pages.strip()}")
            else:
                print("Invalid format in the file. Please ensure each line contains book title, author, release year, and number of pages separated by a comma.")

    def add_book(self):
        book_title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{book_title.strip()}, {author.strip()}, {release_year.strip()}, {num_pages.strip()}"
        self.file.write(book_info + "\n")
        print("Book added successfully!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        contents = self.file.read()
        lines = contents.splitlines()
        books_list = [line.strip() for line in lines]

        index_to_remove = -1
        for index, book in enumerate(books_list):
            if title_to_remove in book:
                index_to_remove = index
                break

        if index_to_remove != -1:
            del books_list[index_to_remove]

            self.file.seek(0)
            self.file.truncate()

            for book in books_list:
                self.file.write(book + "\n")

            print(f"Book '{title_to_remove}' removed successfully!")
        else:
            print(f"Book '{title_to_remove}' not found.")

# Create Library object
lib = Library()

# Menu loop
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
