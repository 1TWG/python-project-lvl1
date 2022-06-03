#!/usr/bin/env python

import random
from brain_games.scripts.games.modules.check_yes_or_no import check_yes_or_no


def even_game():
    q = random.randint(1, 100)
    print('Question:', q)
    answer = check_yes_or_no()
    negative_answer = 'yes' if answer == 'no' else 'no'
    if answer == 'yes' and q % 2 == 0 or answer == 'no' and q % 2 == 1:
        return (True, answer, negative_answer)
    else:
        return (False, answer, negative_answer)
