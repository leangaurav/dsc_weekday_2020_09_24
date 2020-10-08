# WAS that allows you to paas a no as cmd line arg
# and print square of that no.
# square.py


# $ python square.py 10 
# $ 100

# $ python square.py
# $ Please give a no

# $ python square.py 10 20
# $ Please enter only one no

import sys


def square(x):
    if len(x)==2 and x[1].isdigit():
        print(int(x[1])*int(x[1]))

square(sys.argv)