def funct():
    global x
    x = x + 1 # read and write : global
    print("Funct", x) # reading value of x

# python can have multiple variables with same name in different scopes
x = 10 # global x
print(x)
funct()
print(x)