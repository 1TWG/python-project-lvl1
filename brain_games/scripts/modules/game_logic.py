#!/usr/bin/env python

from brain_games.scripts.modules.even_game import even_game
from brain_games.scripts.modules.calc_game import calc_game
from brain_games.scripts.modules.gcd_game import gcd_game
from brain_games.scripts.modules.progression_game import progression_game
from brain_games.scripts.modules.prime_game import prime_game
from brain_games.scripts.modules.check_score import check_score


def game_logic(name, game_flag=0):  # noqa: C901
    score = 0
    game_rules = ['Answer "yes" if the number is even, otherwise answer "no".',
                  'What is the result of the expression?',
                  'Find the greatest common divisor of given numbers.',
                  'What number is missing in the progression?',
                  'Answer "yes" if given number is prime. '
                  'Otherwise answer "no".']
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

        elif game_flag == 3:
            res = progression_game()
            score = check_score(score, res, name)

        elif game_flag == 4:
            res = prime_game()
            score = check_score(score, res, name)
