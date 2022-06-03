#!/usr/bin/env python

def check_number():
    while True:
        st = input('Your answer:')
        if st.isnumeric() or st[1:].isnumeric() and st[0] == '-':
            return st
        else:
            print('Wrong value, write number')
