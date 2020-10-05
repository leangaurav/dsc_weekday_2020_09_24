from random import randrange, uniform
print(randrange(10)) 
print(uniform(10,2))

from random import randint as ri  #aliasing the functin
print(ri(2,4))
#print(randint(2,10)) # this fails here as we have redfined randint to ri