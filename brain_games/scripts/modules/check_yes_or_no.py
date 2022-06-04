#!/usr/bin/env python

import prompt


def check_yes_or_no():
    while True:
        st = prompt.string('Your answer: ')
        if st.lower() == 'yes' or st.lower() == 'no':
            return st.lower()
        else:
            print('Wrong value, write "yes" or "no"')
