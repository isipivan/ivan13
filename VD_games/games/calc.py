import random

ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b}


def get_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(list(ops.keys()))
    answer = str(ops[op](a, b))
    return f"{a} {op} {b}", answer
