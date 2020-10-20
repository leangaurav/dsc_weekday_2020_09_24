###2. Write a program to read itself and print on the screen (Use Command Line Arguments).
import sys
name = sys.argv[0]

f  = open(name, "r")
print(f.read())

f.close()

	