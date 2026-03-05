def play(game):
    print("Welcome to the VD Games!")
    print("May I have your name?", end=" ")
    name = input().strip() or "Anonymous"
    print(f"Hello, {name}!")

    desc = {
        "even": 'Answer "yes" if the number is even, otherwise answer "no".',
        "calc": "What is the result of the expression?",
        "gcd": "Find the greatest common divisor of given numbers.",
        "progression": "What number is missing in the progression?",
        "prime": 'Answer "yes" if given number is prime. Otherwise answer "no".',
    }

    # Получаем имя модуля (even, calc и т.д.)
    module_name = game.__name__.split(".")[-1]
    print(desc[module_name])

    correct = 0
    while correct < 3:
        q, a = game.get_question()
        print(f"Question: {q}")
        print("Your answer:", end=" ")
        u = input().strip()
        if u == a:
            print("Correct!")
            correct += 1
        else:
            print(f"'{u}' is wrong answer ;(. Correct answer was '{a}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
