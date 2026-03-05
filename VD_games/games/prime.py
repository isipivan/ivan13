import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question():
    n = random.randint(1, 50)
    answer = "yes" if is_prime(n) else "no"
    return str(n), answer
