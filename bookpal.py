from classes import BookRead, BookListed, BookGenerator


def main():
    title = BookGenerator.get_text("Book title: ")
    author_first = BookGenerator.get_text("Author's first name: ")
    author_last = BookGenerator.get_text("Author's last name: ")
    review = BookGenerator.get_review()
    quote = BookGenerator.get_quote()
    rating = BookGenerator.get_rating()
    price = BookGenerator.get_price()
    # buy_link = BookGenerator.get_text("Book link (add an URL to your favorite seller): ")
    book = BookRead(
        title=title, 
        format="ebook", 
        author_first_name=author_first, 
        author_last_name=author_last, 
        genre="non-fiction", 
        subgenre="technical", 
        price=price, 
        review=review, 
        quote=quote, 
        rating=rating
        )
    
    # book_two = BookListed(
    #     title=title, 
    #     author_first_name="Brandon", 
    #     author_last_name="Sanderson", 
    #     format="paperback", 
    #     genre="fiction", 
    #     subgenre="fantasy", 
    #     price="12", 
    #     link="https://unicornio.dev",
    #     status="bought"
    #     )
    
    print(book)


if __name__ == "__main__":
    main()