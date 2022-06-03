#!/usr/bin/env python

from brain_games.scripts.games.even_game import even_game
from brain_games.scripts.games.calc_game import calc_game
from brain_games.scripts.games.check_score import check_score


def game_logic(name, game_flag=0):
    score = 0
    game_rules = ['Answer "yes" if the number is even, otherwise answer "no".',
                  'What is the result of the expression?']
    print(game_rules[game_flag])
    while score < 3:
        if game_flag == 0:

            res = even_game()
            score = check_score(score, res, name)

        elif game_flag == 1:
            res = calc_game()
            score = check_score(score, res, name)
