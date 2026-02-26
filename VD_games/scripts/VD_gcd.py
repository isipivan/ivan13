import random
import sys
import math


def main():
    print('Welcome to the VD Games!')
    print('May I have your name?', end=' ')

    try:
        name = input().strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)

    if not name:
        name = 'Anonymous'

    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0
    questions_count = 3

    while correct_answers < questions_count:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)

        correct_answer = math.gcd(num1, num2)

        print(f'Question: {num1} {num2}')
        print('Your answer:', end=' ')

        try:
            user_answer = input().strip()
        except (EOFError, KeyboardInterrupt):
            print()
            print(f"Let's try again, {name}!")
            sys.exit(0)

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
