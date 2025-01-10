# TODO: Add select methods  
# TODO: Migrate error messages to a general dict???

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
        ...

    @classmethod
    def get_price(cls) -> float:
        while True:
            try:
                price = float(input("Book price: ").strip())
                if price >= 0:
                    break
                else:
                    print("Price should be a amount equal to 0 or grater 💸.")
            except ValueError:
                print("Price should be a amount equal to 0 or grater 💸.")
                continue
        return price

    @classmethod
    def get_review(cls) -> str:
        while True:
            review = input("Small review (up to 500 characters): ").strip()
            if len(review) < 2 or len(review) > 500:
                print("Book reviews should have at least 2 characters and a maximum of 500 characters 😫.")
            else:
                break
        return review
    
    @classmethod
    def get_quote(cls) -> str:
        while True:
            quote = input("Favorite quote (up to 200 characters): ").strip()
            if len(quote) < 2 or len(quote) > 200:
                print("Book quotes should have at least 2 characters and a maximum of 200 characters 😥.")
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
                   print("Rating should be an integer number between 1 and 5 🥲.") 
            except ValueError:
                print("Rating should be an integer number between 1 and 5 🥲.")
                continue
        return rating