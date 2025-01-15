from pick import pick
from rich.console import Console

console = Console()

from classes import BookListed, BookRead
from utils import get_genres, get_subgenres, get_statuses, get_formats, url_validator

class BookGenerator:
    @classmethod
    def get_text(cls, input_msg: str) -> str:
        while True:
            user_input = input(input_msg).strip()
            if len(user_input) > 1:
                break
        return user_input

    @classmethod
    def get_selection(cls, selection_list: list[str]) -> str:
        title = "Please select the right value:"
        option, _ = pick(selection_list, title)
        return option

    @classmethod
    def get_price(cls) -> float:
        while True:
            try:
                price = float(input("Book price: ").strip())
                if price >= 0:
                    break
                else:
                    console.print("[bold red]Price should be a amount equal to 0 or grater[/bold red] 💸.")
            except ValueError:
                console.print("[bold red]Price should be a amount equal to 0 or grater[/bold red] 💸.")
                continue
        return price

    @classmethod
    def get_review(cls) -> str:
        while True:
            review = input("Small review (up to 500 characters): ").strip()
            if len(review) < 2 or len(review) > 500:
                console.print("[bold red]Book reviews should have at least 2 characters and a maximum of 500 characters[/bold red] 😫.")
            else:
                break
        return review
    
    @classmethod
    def get_quote(cls) -> str:
        while True:
            quote = input("Favorite quote (up to 200 characters): ").strip()
            if len(quote) < 2 or len(quote) > 200:
                console.print("[bold red]Book quotes should have at least 2 characters and a maximum of 200 characters[/bold red] 😥.")
            else:
                break
        return quote

    @classmethod
    def get_rating(cls) -> int:
        while True:
            try:
                rating =  int(input("Book review ⭐ (Enter a number between 1 and 5): ").strip())
                if rating >= 1 and rating <= 5:
                    break
                else:
                   console.print("[bold red]Rating should be an integer number between 1 and 5[/bold red] 🥲.") 
            except ValueError:
                console.print("[bold red]Rating should be an integer number between 1 and 5[/bold red] 🥲.")
                continue
        return rating
    
    @classmethod
    def get_link(cls) -> str:
        while True:
            link = input("Add a link to the book seller: ")
            if not link:
                console.print("[bold red]Missing book link[/bold red] 😫")
            match = url_validator(link)
            if match:
                break
            else:
                console.print("[bold red]Link should be a URL[/bold red] 🥲")
                continue
        return link

    @classmethod
    def generate_book(cls, type: str) -> BookListed | BookRead:
        title = cls.get_text("Book title: ")
        author_first = cls.get_text("Author's first name: ")
        author_last = cls.get_text("Author's last name: ")
        price = cls.get_price()
        if type == "read":
            rating = cls.get_rating()
            review = cls.get_review()
            quote = cls.get_quote()
            genre = cls.get_selection(get_genres())
            subgenre = cls.get_selection(get_subgenres(genre))
            format = cls.get_selection(get_formats())
            return BookRead(
                title=title, 
                author_first_name=author_first, 
                author_last_name=author_last, 
                price=price, 
                rating=rating,
                genre=genre, 
                subgenre=subgenre, 
                review=review, 
                format=format, 
                quote=quote, 
            )
        elif type == "listed":
            link = cls.get_link()
            genre = cls.get_selection(get_genres())
            subgenre = cls.get_selection(get_subgenres(genre))
            format = cls.get_selection(get_formats())
            status = cls.get_selection(get_statuses())
            return BookListed(
                title=title,
                author_first_name=author_first,
                author_last_name=author_last,
                genre=genre,
                subgenre=subgenre,
                price=price,
                format=format,
                link=link,
                status=status,
            )
        else:
            console.print("[bold red]Book type should be: 'listed' or 'read'[/bold red]")