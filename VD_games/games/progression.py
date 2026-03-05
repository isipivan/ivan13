import random


def get_question():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    prog = [str(start + i * step) for i in range(length)]
    pos = random.randint(0, length - 1)
    answer = prog[pos]
    prog[pos] = ".."
    return " ".join(prog), answer
