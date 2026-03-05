import random
import math


def get_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    answer = str(math.gcd(a, b))
    return f"{a} {b}", answer
