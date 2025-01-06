from classes import Book


def main():
    book = Book(title="Hola", format="ebook", author_first_name="ann", author_last_name="diaz", genre="non-fiction", subgenre="technical", price="25.99")
    book_two = Book(title="Rhythm of War", author_first_name="Brandon", author_last_name="Sanderson", format="paperback", genre="fiction", subgenre="fantasy", price="12")
    print(book, book_two)


if __name__ == "__main__":
    main()