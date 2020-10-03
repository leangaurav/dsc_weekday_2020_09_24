print("Assignment_Intro")

# Prog1
s1 = "Harshith"
s2 = "harshithprabhakar@gmail.com"
print(len(s1),len(s2))

# Prog2
in_data = input("Enter string : ")
print(in_data)

# Prog3
num1 = int(input("Num1 :"))
num2 = int(input("Num2 :"))
print(num1 + num2)
print(num1 - num2)

# Prog4
s1 = "abc"
s2 = "def"
s3 = s1 + s2
print(s3)

# Prog 5
s1 = "abc"
s2 = "def"
s3 = s1 + s2
print(s3)

# Prog 6
s1 = "abc" * 4
print(s1)

# Prog 7
s1 = "abc\n" * 4
print(s1)

# Prog 8
s = input("Enter a string : ")
s1 = s+"\n"
n = int(input("Enter a number : "))
print(s1*n)

# Prog 9
res = print("Harshith")
print(res, type(res))

# Prog 10
res = len("harshithprabhakar@gmail.com")
print(type(res))

# Prog 11
s1 = "Harshith"
s2 = "harshithprabhakar@gmail.com"
s3 = s1 + "\n" + s2
print(type(s3))
print(len(s3))

# Prog 12
import math
num = int(input("Enter a number to find the square : "))
print(math.sqrt(num))

# Prog 13
import math
num = int(input("Enter a number to find the square : "))
print(math.sqrt(num))

# Prog 14
num1 = int(input("Num1 : "))
num2 = int(input("Num2 : "))
num3 = int(input("Num3 : "))
num4 = int(input("Num4 : "))
print((num1+num2+num3+num4)/4)

# Prog 15
num_int = -304
num_float = -56.78
num_complex = (3-4j)
print(abs(num_int))
print(abs(num_float))
print(abs(num_complex))

# Prog 16
print(__name__)
# output --> __main__

# Prog 17
print(__name__)
# output --> __main__

# Prog 18
# dir(int) does not contain "__name__"

# Prog 19
print(__name__)
print(__builtins__.__name__)
print(int.__name__)

