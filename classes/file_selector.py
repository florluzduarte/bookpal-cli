from rich.console import Console

from classes import BookRead, BookListed, BookGenerator

console = Console()

class FileSelector:
    @classmethod
    def print_info(cls) -> None:
        return console.print(":backhand_index_pointing_right: Which file do you wish to update?")
    
    @classmethod
    def get_file_name(cls) -> str:
        while True:
            file_name = input("File name ('finished-books' or 'wishlist-books'): ").strip()
            if file_name == "finished-books" or file_name == "wishlist-books":
                break
            else: 
                console.print("[bold red]Files available are: 'finished-books' or 'wishlist-books'[/bold red] 😫")
                continue
        return file_name