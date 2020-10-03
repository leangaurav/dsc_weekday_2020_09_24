def funct():
    x = 100 # local x
    print(x) # reading value of x

# python can have multiple variables with same name in different scopes
x = 10 # global x
print(x)    
funct()
print(x)