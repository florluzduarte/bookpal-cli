from utils import get_app_title
from classes import BookGenerator
from rich.console import Console


def main(): 
    console = Console()
    console.print(f"[violet]{get_app_title()}[/violet]")
    console.print("[aquamarine1]A CLI program to organize your reading lists.[/aquamarine1]")
    console.print("[aquamarine1]Made with love and Python by Flor Luz Duarte.[/aquamarine1]")
    print(" ")
    book = BookGenerator.generate_book("read")
    print(book)


if __name__ == "__main__":
    main()