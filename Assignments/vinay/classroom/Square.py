# WAS that allows you to paas a no as cmd line arg
# and print square of that no.
# square.py


# $ python square.py 10 
# $ 100

# $ python square.py
# $ Please give a no

# $ python square.py 10 20
# $ Please enter only one no
import sys

if(len(sys.argv)== 1):
	print("give a number")
elif(len(sys.argv) > 2):
		print ("only one arg")
else:
	print(int(sys.argv[1])**2)