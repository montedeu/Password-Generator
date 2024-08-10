import string
import secrets


def contains_upper(password: str) -> bool:
    """Checks whether password contains uppercase or not."""
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    """Checks whether password contains symbols or not."""
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    """
    Generates a random password based on user specifications.

    :param length: The length of the password.
    :param symbols: Whether the password contains symbols or not.
    :param uppercase: Whether the password contains uppercase or not.
    :return: A random password.
    """

    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    # Check to make sure that user specifications were met.
    while contains_symbols(new_password) != symbols or contains_upper(new_password) != uppercase:
        new_password = ''
        for _ in range(length):
            new_password += combination[secrets.randbelow(combination_length)]

    return new_password


def main() -> None:
    for i in range(1, 6):
        new_pass: str = generate_password(length=3, symbols=False, uppercase=False)
        specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')


if __name__ == "__main__":
    main()
