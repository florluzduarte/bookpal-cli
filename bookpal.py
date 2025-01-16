from utils import get_app_title
from classes import FileSelector, CommandHandler
from rich.console import Console


def main(): 
    console = Console()
    console.print(f"[violet]{get_app_title()}[/violet]")
    console.print("[aquamarine1]A CLI program to organize your reading lists.[/aquamarine1]")
    console.print("[aquamarine1]Made with love and Python by Flor Luz Duarte.[/aquamarine1]")
    print(" ")
    print(" ")
    FileSelector.print_info()
    file = FileSelector.get_file_name()
    print(" ")
    console.print(f"[violet]Selected file: {file}[/violet]")
    command = CommandHandler.get_command()
    console.print(f"[violet]Selected command: {command}[/violet]")
    print(" ")
    CommandHandler.execute(command=command, file_name=file)
    print(" ")

if __name__ == "__main__":
    main()