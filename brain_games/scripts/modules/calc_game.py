#!/usr/bin/env python

import random
from brain_games.scripts.modules.check_number import check_number


def calc_game():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    flag = random.randint(0, 2)
    if flag == 0:
        print(f'Question: {a} + {b}')
        res = a + b
    elif flag == 1:
        print(f'Question: {a} - {b}')
        res = a - b
    elif flag == 2:
        print(f'Question: {a} * {b}')
        res = a * b
    answer = check_number()

    if int(answer) == (res):
        return (True, answer, res)
    else:
        return (False, answer, res)
