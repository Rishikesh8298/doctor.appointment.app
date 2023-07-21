from random import shuffle, choices
from string import digits, ascii_lowercase, ascii_uppercase


def password_generator():
    lower_letter = choices([i for i in ascii_lowercase], k=4)
    digit = choices([i for i in digits], k=3)
    upper_letter = choices([i for i in ascii_uppercase], k=1)
    new_password = lower_letter + digit + upper_letter
    shuffle(new_password)
    return "".join(new_password)
