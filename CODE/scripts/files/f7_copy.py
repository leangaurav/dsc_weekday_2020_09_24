import sys

if len(sys.argv) != 3:
    print("Invalid input")
    exit()

name1 = sys.argv[1]
name2 = sys.argv[2]

f1  = open(name1, "r")
s  = f1.read()
f2  = open(name2, "w")
f2.write(s)

f1.close()
f2.close()