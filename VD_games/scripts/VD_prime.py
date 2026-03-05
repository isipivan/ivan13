import random
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print('Welcome to the VD Games!')
    print('May I have your name?', end=' ')
    name = input().strip() or 'Anonymous'
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct = 0
    while correct < 3:
        n = random.randint(1, 50)
        a = 'yes' if is_prime(n) else 'no'
        print(f'Question: {n}')
        print('Your answer:', end=' ')
        u = input().strip().lower()
        if u == a:
            print('Correct!')
            correct += 1
        else:
            print(f"'{u}' is wrong answer ;(. Correct answer was '{a}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
