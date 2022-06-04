#!/usr/bin/env python

from brain_games.scripts.modules.welcome_user import welcome_user
from brain_games.scripts.modules.game_logic import game_logic


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    game_logic(player_name, 3)
    print(f'Congratulations, {player_name}!!!')


if __name__ == '__main__':
    main()