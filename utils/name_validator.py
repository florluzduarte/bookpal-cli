def name_validator(name):
    if len(name) < 2:
        raise ValueError("Invalid Author's name. It should be longer than 2 characters 🫠.")
    if not name.isalpha():
        raise ValueError("Invalid Author's name. All characters should be alphabetical 😥.")
    return True