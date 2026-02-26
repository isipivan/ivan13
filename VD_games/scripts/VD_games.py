from VD_games.cli import welcome


def start_game():
    return "Game started!"


def main():
    name = welcome()
    print(f'Hello, {name}!')
    print(start_game())


if __name__ == '__main__':
    main()
