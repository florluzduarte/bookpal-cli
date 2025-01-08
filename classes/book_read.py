from classes import Book;


class BookRead(Book):
    def __init__(
            self, 
            title, 
            author_first_name, 
            author_last_name, 
            genre, 
            subgenre, 
            price, 
            format, 
            rating,
            review,
            quote
            ):
        super().__init__(title, author_first_name, author_last_name, genre, subgenre, price, format)
        self.rating = rating
        self.review = review
        self.quote = quote
    
    def __str__(self):
        return f"""
        ======

        📚 Title: {self.title}
        🤓 Author: {self.author_first_name} {self.author_last_name}
        ✨ Genre: {self.genre.capitalize()}
        🔍 Subgenre: {self.subgenre.capitalize()}
        💸 Price: ${self.price}
        ✍️  Format: {self.format.capitalize()}
        ✨ Rating: {'⭐' * self.rating}
        🗒️  Review: {self.review}
        😊 Quote: {self.quote}
        """

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if not rating:
            raise ValueError("Missing book rating 🫠")
        if rating < 1 or rating > 5:
            raise ValueError("Rating value should be between 1 and 5 🥲")
        self._rating = rating

    @property
    def review(self):
        return self._review
    
    @review.setter
    def review(self, review):
        if not review:
            raise ValueError("Missing book review 🥲") 
        if len(review) > 500:
            raise ValueError("Reviews are up to 500 characters 🫠")
        self._review = review

    @property
    def quote(self):
        return self._quote
    
    @quote.setter
    def quote(self, quote):
        if len(quote) > 200:
            raise ValueError("Quotes are up to 200 characters 🥲")
        self._quote = quote