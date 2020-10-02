def funct():
    global x
    print("Funct", x)
    x = 100
    print("Funct", x) # reading value of x

# python can have multiple variables with same name in different scopes
x = 10 # global x
print(x)    
funct()
print(x)