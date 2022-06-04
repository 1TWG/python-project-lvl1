#!/usr/bin/env python

import random
from brain_games.scripts.modules.check_yes_or_no import check_yes_or_no


def prime_game():
    a = random.randint(1, 100)
    print(f'Question: {a}')
    res = 'yes'
    for i in range(2, a):
        if a % i == 0:
            res = 'no'

    answer = check_yes_or_no()

    if (answer) == (res):
        return (True, answer, res)
    else:
        return (False, answer, res)
