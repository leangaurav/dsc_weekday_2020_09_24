import cmath           # cmath is a module which contains sqrt function
print(cmath.sqrt(-1))  # it will execute

import math            # math  is a module which also contains sqrt function
print(math.sqrt(-1))    #it won't execute, overlapping error  

# As both modules have same function name, so it is necessary to call function by their modules for ex- "module.function name", otherwise if will call sqrt function directly, it will confuse in between 2 modules 
# This will throw error

    # ERROR
# /*1j
 # Traceback (most recent call last):
   # File "f6_overlapping_import.py", line 5, in <module>
     # print(math.sqrt(-1))
# ValueError: math domain error*/  