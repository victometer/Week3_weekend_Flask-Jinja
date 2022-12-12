from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book_at_index
from models.book import *


@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books', methods = ['POST'])
def create():
    title = request.form["title"]
    genre = request.form["genre"]
    author = request.form["author"]
    # description = request.form["description"]
    # recurring = request.form["recurring"]
    new_book = Book(title, genre, author)
    add_new_book(new_book)
    return redirect('/books')

@app.route('/<index>')
def single_index(index):
    single_book = books[int(index)]
    return render_template('single_book_index.html', single_book=single_book)

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
    delete_book_at_index(int(index))
    return redirect('/books')
