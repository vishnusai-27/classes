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
    

book1 = Media("Ugly love", "Ana hung", True)
print(book1.title)