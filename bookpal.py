from classes import BookRead, BookListed


def main():
    book = BookRead(
        title="Hola", 
        format="ebook", 
        author_first_name="ann", 
        author_last_name="diaz", 
        genre="non-fiction", 
        subgenre="technical", 
        price="25.99", 
        review="Me encantó", 
        quote="Todo es lindo", 
        rating=4
        )
    
    book_two = BookListed(
        title="Rhythm of War", 
        author_first_name="Brandon", 
        author_last_name="Sanderson", 
        format="paperback", 
        genre="fiction", 
        subgenre="fantasy", 
        price="12", 
        link="https://unicornio.dev",
        status="Bought"
        )
    
    print(book, book_two)


if __name__ == "__main__":
    main()