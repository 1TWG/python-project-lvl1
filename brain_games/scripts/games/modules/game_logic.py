#!/usr/bin/env python

from brain_games.scripts.games.modules.even_game import even_game
from brain_games.scripts.games.modules.calc_game import calc_game
from brain_games.scripts.games.modules.gcd_game import gcd_game
from brain_games.scripts.games.modules.check_score import check_score


def game_logic(name, game_flag=0):
    score = 0
    game_rules = ['Answer "yes" if the number is even, otherwise answer "no".',
                  'What is the result of the expression?',
                  'Find the greatest common divisor of given numbers.']
    print(game_rules[game_flag])
    while score < 3:
        if game_flag == 0:

            res = even_game()
            score = check_score(score, res, name)

        elif game_flag == 1:
            res = calc_game()
            score = check_score(score, res, name)

        elif game_flag == 2:
            res = gcd_game()
            score = check_score(score, res, name)
