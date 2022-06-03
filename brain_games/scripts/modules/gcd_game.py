#!/usr/bin/env python

import random
from brain_games.scripts.modules.check_number import check_number


def gcd_game():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f'Question: {a} and {b}')
    res = 1
    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            res = i

    answer = check_number()

    if int(answer) == (res):
        return (True, answer, res)
    else:
        return (False, answer, res)
