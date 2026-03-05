import random


def is_even(n):
    return n % 2 == 0


def get_question():
    n = random.randint(1, 100)
    answer = "yes" if is_even(n) else "no"
    return str(n), answer
