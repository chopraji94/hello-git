"""Q.1- Write a python code to find a valid email address from a text."""

s = input('Enter a mobile number to validate: ')

m = re.fullmatch('^[a-zA-Z0-9_.+-]+[@](gmail.com|yahoo.com)', s)

if m:
    print(s, 'It is vaid Email id')
else:
    print(s, 'not valid')

"""Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )"""

import re

s = input('Enter a mobile number to validate: ')

m = re.fullmatch('[+]\d[91]-[6-9]\d{9}', s)

if m:
    print(s, 'It is vaid indian number')
else:
    print(s, 'not valid')
