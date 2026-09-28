class Media:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def check_out(self):
        self.is_checked_out = True

    def return_item(self):
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title}, {self.author}"

class Book(Media):
    def __init__(self, title, author, is_checked_out, page_count, isbn):
        super().__init__(title, author, is_checked_out)
        self.page_count = page_count
        self.isbn = isbn

    def __str__(self):
        return f"{self.title}, {self.author} ({self.page_count} pages)"

class Magazine(Media):
    def __init__(self, title, author, is_checked_out, issue_number):
        super().__init__(title, author, is_checked_out)
        self.issue_number = issue_number

    def __str__(self):
        return f"{self.title}, {self.author} ({self.issue_number} number)"

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def check_out_item(self, title):
        for self.item in self.items:
            if self.title == title:
                if self.item.is_checked_out:
                    print(f"'{title}' is already checked out.")
                else:
                    self.item.check_out()
                    print(f"'{title}' checked out.")
            return
        print(f"{self.title} not found in the library.")

    def return_item(self, title):
        for self.item in self.items:
            if self.title == title:
                if not self.item.is_checkedout:
                    print(f"'{title}' was not checked out.")
                else:
                    self.item.return_item()
                    print(f"{self.title} has been returned.")
            return
        print(f"{self.title} not found in the library.")

    def list_available_items(self):
        available = False
        for self.item in self.items:
            if not self.item.checked_out:
                print(self.item)
                available = True
        if not available:
            print("No Items available.")
        pass
    

book1 = Media("Ugly love", "Ana hung", True)
print(book1.title)