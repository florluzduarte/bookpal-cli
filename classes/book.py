# TODO: generar la clase base Book
# TODO: Definir getters, setters y manejo de errores para todas las properties de Book
# TODO: generar las clases heredadas BookRead y BookListed
# TODO: definir getters, setters y manejo de errores de las properties de las clases con herencia

from utils import name_validator


class Book:
    def __init__(self, title, author_first_name, author_last_name, genre, price, format):
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.genre = genre
        self.price = price
        self.format = format
    
    def __str__(self):
        return f"Title: {self.title}"

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

