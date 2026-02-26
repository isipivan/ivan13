import random
import sys


def is_even(number):
    return number % 2 == 0


def main():
    print('Welcome to the VD-games!')
    print('May I have your name?', end=' ')

    try:
        name = input().strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)

    if not name:
        name = 'Anonymous'

    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    questions_count = 3

    while correct_answers < questions_count:
        number = random.randint(1, 100)
        correct_answer = 'yes' if is_even(number) else 'no'

        print(f'Question: {number}')
        print('Your answer:', end=' ')

        try:
            user_answer = input().strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            print(f"Let's try again, {name}!")
            sys.exit(0)

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
