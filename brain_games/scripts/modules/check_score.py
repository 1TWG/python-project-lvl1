#!/usr/bin/env python

def check_score(score, res, name):  # example (True, answer, 'no')
    if res[0]:
        score += 1
        print('Correct!')
        return score
    else:
        print(f"'{res[1]}' is wrong answer ;(. Correct answer was '{res[2]}'.")
        print(f'Let\'s try again, {name}!')
        return 0
