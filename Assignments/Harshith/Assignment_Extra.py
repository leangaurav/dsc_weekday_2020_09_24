print("Assignment_Extra")

# Prog1
temp_Fahrenhiet = float(input("Enter the temperature in  Fahrenhiet : "))
print((temp_Fahrenhiet-32)*5/9)

# Prog2
num = int(input("Enter a number to calculate square and cube : "))
square = num*num
cube = num*num*num
print("Square : " + str(square))
print("Cube : " + str(cube))

# Prog3
n = int(input("n : "))
m = int(input("m : "))
print((n*n)+(m*m))
print(pow(n,2)+pow(m,2))


# Prog4
n = int(input("n : "))
m = int(input("m : "))
print(m**n) #m power n
print(pow(m,n))

# Prog5
p = float(input("Principal : "))
t = int(input("Time : "))
r = float(input("Rate of interest : "))
simple_Interest = (p*t*r)/100
print("Simple Interest : " + str(simple_Interest))

# # Prog6


# # Prog7 - sum of first n natural numbers
n = int(input("n : "))
num = 1
sum = 0
while(num<=n):
    sum = sum + num
    num = num + 1
print(sum)

# # Prog8 - i) Swap numbers using temp
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
temp = num1
num1 = num2
num2 = temp
print("Num1 :" + str(num1))
print("Num2 :" + str(num2))

# # Prog8 - ii) Swap numbers in pythonic way
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
num1, num2 = num2, num1
print("Num1 :" + str(num1))
print("Num2 :" + str(num2))

# # Prog9
print(ord(' '))

# # Prog10
char = input("Enter a character to find the ASCII value :")
print(ord(char))

# # Prog11 - Area of Circle
area_of_circle = float(input("Enter area of circle : "))
import math
radius = math.sqrt(area_of_circle/3.14)
circumference = 2 * 3.14 * radius
print("Radius of circle : " + str(radius))
print("Circumference of circle : " + str(circumference))

# # Prog12 -
print("Enter marks in following subjects")
maths = int(input("Maths : "))
science = int(input("Science : "))
social = int(input("Social : "))
english = int(input("English : "))
comp = int(input("Comp : "))
percentage = ((maths + science + social + english + comp) / 500) * 100
print("Percentage : " + str(percentage))