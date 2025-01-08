from classes import Book
from utils import get_statuses, url_validator


class BookListed(Book):
    def __init__(
            self,
            title, 
            author_first_name, 
            author_last_name, 
            genre, 
            subgenre, 
            price, 
            format,
            link,
            status
            ):
        super().__init__(title, author_first_name, author_last_name, genre, subgenre, price, format)
        self.link = link
        self.status = status 

    def __str__(self):
        return f"""
        ======

        📚 Title: {self.title}
        🤓 Author: {self.author_first_name} {self.author_last_name}
        ✨ Genre: {self.genre.capitalize()}
        🔍 Subgenre: {self.subgenre.capitalize()}
        💸 Price: ${self.price}
        ✍️  Format: {self.format.capitalize()}
        🔗 Link: {self.link}
        🗒️  Status: {self.status}
        """

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        if not link:
            raise ValueError("Missing book link 😫")
        match = url_validator(link)
        if match:
            self._link = link
        else:
            raise ValueError("Link should be a URL 🥲")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        statuses = get_statuses()
        if not status:
            raise ValueError("Missing book status 🥲")
        if status not in statuses:
            raise ValueError("Invalid status 😫. Valid values are: Bought, To buy, Rented, To rent")
        self._status = status