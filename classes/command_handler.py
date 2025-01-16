from pick import pick
from rich.console import Console

console = Console()

from utils import get_commands
from classes import BookListed, BookRead, BookGenerator


class CommandHandler:
    @classmethod
    def get_command(cls) -> str:
        title = "Please select a command to start. (For more information select --help)."
        option, _ = pick(get_commands(), title)
        return option
    
    @classmethod
    def execute(cls, command: str, file_name: str) -> None:
        if not command:
            raise ValueError("Missing command 🥲.")
        if not file_name:
            raise ValueError("Missing file name 🫠.")
        if command not in get_commands():
            raise ValueError("Invalid command 😫.")
        if file_name not in ["finished-books", "wishlist-books"]:
            raise ValueError("Invalid file name 💀. Available files are: 'finished-books' and 'wishlist-books'")
        match command:
            case "--add":
                book = cls.add(file_name=file_name)
                print(" ")
                console.print("[violet]Book added successfully[/violet]")
                print(book)
                print(" ")
            case "--search":
                print("--search")
            case "--delete":
                print("--delete")
            case "--edit":
                print("--edit")
            case "--amount":
                print("--amount")
            case "--reset":
                print("--reset")
            case "--print":
                print("--print")
            case "--help":
                cls.help()
            case _:
                raise ValueError("Invalid command 🥲.")
    
    @classmethod
    def add(cls, file_name: str) -> BookListed | BookRead:
        if file_name == "wishlist-books":
            book = BookGenerator.generate_book(type="listed")
        else:
            book = BookGenerator.generate_book(type="read")
        return book
    
    @classmethod
    def help(cls) -> None:
        console.print("[aquamarine1]----- BOOKPAL HELP -----[/aquamarine1]")
        print(" ")
        print(
        """
        👉 Files and usage:
        1. finished-books: A list to track all the books you've read.
        2. wishlist-books: A list to track all the books you wish to buy or rent. 

        👉 Commands:
        Both types of files offer the same commands with identical functionality.
        1. --add: Add a new book to the selected list.
        2. --search: Allows you to search books using one of the following parameters: 
        Author's last name, author's first name, book genre, book rating, book name and book ID
        3. --delete: You can remove books from your lists using this command.
        4. --edit: Allows you to change a book record.
        5. --amount: Returns the amount of money you've spend on the finished books list 
        or the amount of money you need to buy your entire wishlist.
        6. --reset: Deletes all entries in the selected file. 
        Use carefully and try to avoid it if you can.
        7. --print: Prints all the books in the selected list.
        8. --help: Shows useful information about the program and its use cases.

        👉 About the project: 
        BookPal was created as a helpfull companion for avid readers.
        It allows you to keep all your books in one place.
        Also you can export the lists on different formats such as PDF and Markdown.

        👉 Errors and Bugs:
        This is an open source project, if you wish to report a bug 
        or collaborate you can do so via GitHub.
        You'll find more information here: https://github.com/florluzduarte/bookpal-cli

        👉 Credits: 
        Software Developer and creator: 
        Florencia Luz Duarte (https://unicornio.dev/en)
        """
        )
        print(" ")
        console.print("[aquamarine1]----- HAPPY READING :) -----[/aquamarine1]")
