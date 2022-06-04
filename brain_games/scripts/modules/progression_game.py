#!/usr/bin/env python

import random
from brain_games.scripts.modules.check_number import check_number


def progression_game():
    len_progression = random.randint(5, 15)
    quest_position = random.randint(0, len_progression - 1)
    coef = random.randint(1, 20)
    progression = [i * coef for i in list(range(1, len_progression + 1))]
    res = progression[quest_position]
    quest_list = progression[0:quest_position] + ['..'] + progression[quest_position + 1:]
    print(f'Question:', end=' ')
    for i in quest_list:
        print(i, end=' ')
    print()

    answer = check_number()

    if int(answer) == (res):
        return (True, answer, res)
    else:
        return (False, answer, res)
