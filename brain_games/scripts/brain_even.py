#!/usr/bin/env python

import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name


def main():
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    start_game(player_name)


def check_yes_or_no():
    while True:
        st = input()
        if st.lower() == 'yes' or st.lower() == 'no':
            return st
        else:
            print('Wrong value, write "yes" or "no"')


def game():
    q = random.randint(0, 100)
    print('Question:', q)
    answer = check_yes_or_no()
    if answer == 'yes' and q % 2 == 0 or answer == 'no' and q % 2 == 1:
        return (True, answer)
    else:
        return (False, answer)


def start_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    check_answer = 0
    while check_answer < 3:
        res = game()
        if res[0]:
            check_answer += 1
            print('Correct!')
        else:
            check_answer = 0
            print(res[1], ' is wrong answer ;(.')
            print('Let\'s try again,', name)
    print('Congratulations,', name)


if __name__ == '__main__':
    main()
