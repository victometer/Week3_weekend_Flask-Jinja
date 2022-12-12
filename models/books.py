from models.book import *

book1 = Book ("Wuthering Heights", 'classic', 'Emily Bronte')
book2 = Book ('Harry Potter', "fantasy", "J.K.Rowling")
book3 = Book ('Game of Thrones', 'fantasy', "G.R.R. Martin")

books = [book1, book2, book3]


def add_new_book(book):
    books.append(book)

def delete_book_at_index(index):
    books.pop(index)