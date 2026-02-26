import random
import sys


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def main():
    print('Welcome to the VD games!')
    print('May I have your name?', end=' ')

    try:
        name = input().strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)

    if not name:
        name = 'Anonymous'

    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    operators = ['+', '-', '*']
    correct_answers = 0
    questions_count = 3

    while correct_answers < questions_count:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(operators)

        correct_result = calculate(num1, num2, operator)

        print(f'Question: {num1} {operator} {num2}')
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
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_result:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
