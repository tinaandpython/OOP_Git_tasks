
class Books:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        print(f"Title: {self.title}")

    def get_author(self):
        print(f"Author: {self.author}")


PP = Books("Pride and Prejudice", "Jane Austen")
H = Books("Hamlet", "William Shakespeare")
WP = Books("War and Peace", "Leo Tolstoy")


H.get_title()
H.get_author()