# TODO: Definir getters, setters y manejo de errores para todas las properties de Book
# TODO: generar las clases heredadas BookRead y BookListed
# TODO: definir getters, setters y manejo de errores de las properties de las clases con herencia

import sys

from utils import name_validator, get_genres, get_subgenres, get_formats


class Book:
    def __init__(self, title, author_first_name, author_last_name, genre, subgenre, price, format):
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.genre = genre
        self.subgenre = subgenre
        self.price = price
        self.format = format
    
    def __str__(self):
        return f"""
        ======

        📚 Title: {self.title}
        🤓 Author: {self.author_first_name} {self.author_last_name}
        ✨ Genre: {self.genre.capitalize()}
        🔍 Subgenre: {self.subgenre.capitalize()}
        💸 Price: ${self.price}
        ✍️  Format: {self.format.capitalize()}
        """

    @property
    def title(self):
        return self._title  
    
    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Missing book title 🥲")
        self._title = title.strip().capitalize()
    
    @property
    def author_first_name(self):
        return self._author_first_name
    
    @author_first_name.setter
    def author_first_name(self, author_first_name):
        if not author_first_name:
            raise ValueError("Missing Author's first name 😥.")
        if name_validator(author_first_name):
            self._author_first_name = author_first_name.strip().capitalize()

    @property 
    def author_last_name(self):
        return self._author_last_name

    @author_last_name.setter
    def author_last_name(self, author_last_name):
        if not author_last_name:
            raise ValueError("Missing Author's last name 😥.")
        if name_validator(author_last_name):
            self._author_last_name = author_last_name

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, genre):
        genres = get_genres()
        if not genre:
            raise ValueError("Missing genre 😥.")
        if genre not in genres:
            raise ValueError("Invalid genre 😣. Valid genres are: drama, fiction, non-fiction or poetry.")
        self._genre = genre

    @property
    def subgenre(self):
        return self._subgenre
    
    @subgenre.setter
    def subgenre(self, subgenre):
        valid_subgenres = get_subgenres(self.genre)
        if not subgenre:
            raise ValueError("Missing subgenre 🥲.")
        if subgenre not in valid_subgenres:
            raise ValueError("Invalid subgenre 🫠.")
        self._subgenre = subgenre

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        try:
            float(price)
        except ValueError:
            sys.exit("Price is not a number, or the format is invalid 😣.")
        if not price:
            raise ValueError("Missing price 💸.")
        if float(price) < 0:
            raise ValueError("Price should be a positive number 😫.")
        self._price = f"{float(price):,.2f}"
    
    @property
    def format(self):
        return self._format
    
    @format.setter
    def format(self, format):
        valid_formats = get_formats()
        if not format:
            raise ValueError("Missing format 😶.")
        if format not in valid_formats:
            raise ValueError("Invalid format 😫. Available formats are: paperbook, hardcover, ebook, audiobook and pdf")
        self._format = format
