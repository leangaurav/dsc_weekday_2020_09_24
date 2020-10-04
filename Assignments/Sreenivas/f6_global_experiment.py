def fun():
#	x = 100
#   print(x)
    global x
    x = 10
    print(x)

x = 5
print(x)
fun()
print(x)