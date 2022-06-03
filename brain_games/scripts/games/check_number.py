#!/usr/bin/env python

def check_number():
    while True:
        st = input('Your answer:')
        if st.isnumeric():
            return st
        else:
            print('Wrong value, write number')
