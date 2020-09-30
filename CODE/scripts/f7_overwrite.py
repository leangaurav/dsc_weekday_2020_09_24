from cmath import *
print(sqrt(-1))

from math import * # overwrites the one imported from
print(sqrt(-1)) 

 # ERROR
 # /* 1j
# Traceback (most recent call last):
  # File "f7_overwrite.py", line 5, in <module>
    # print(sqrt(-1))
# ValueError: math domain error*/ 