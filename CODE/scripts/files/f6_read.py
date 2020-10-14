import sys

name = sys.argv[0]

f  = open(name, "r")
print(f.read())

f.close()