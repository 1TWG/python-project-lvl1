#!/usr/bin/env python

from brain_games.scripts.games.welcome_user import welcome_user
from brain_games.scripts.games.game_logic import game_logic


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    game_logic(player_name, 0)
    print(f'Congratulations, {player_name}!!!')


if __name__ == '__main__':
    main()
