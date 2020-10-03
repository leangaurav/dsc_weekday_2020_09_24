x = 10 # global scope
print(x)

def funct():
    print(x) # reading value of x
    #print(y)
    
funct()