import random
import sys

def make_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    progression = [str(start + i * step) for i in range(length)]
    pos = random.randint(0, length - 1)
    answer = progression[pos]
    progression[pos] = '..'
    return ' '.join(progression), answer

def main():
    print('Welcome to the VD Games!')
    print('May I have your name?', end=' ')
    name = input().strip() or 'Anonymous'
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    correct = 0
    while correct < 3:
        q, a = make_progression()
        print(f'Question: {q}')
        print('Your answer:', end=' ')
        u = input().strip()
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
