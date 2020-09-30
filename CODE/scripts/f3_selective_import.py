from random import randrange, randint, uniform  # selective import

print(randrange(1,10))
print(randint(1,10))
print(uniform(2,4)) #The uniform() method returns a random floating number between the two specified numbers (both included).

from random import randint as ri # alias name for  randint
print("RI:", ri(10,15)) 
 