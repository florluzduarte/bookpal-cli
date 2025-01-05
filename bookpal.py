from classes import Book


def main():
    book = Book(title="Hola", format="ebook", author_first_name="ann", author_last_name="diaz", genre="horror", price=25)
    print(book)


if __name__ == "__main__":
    main()