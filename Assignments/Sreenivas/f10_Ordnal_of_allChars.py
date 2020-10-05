def Ord_Value(myString):
    i = 0
    while( i < len(myString)):
        print(myString[i],ord(myString[i]))
        i += 1

GetString = input("Enter a string:")
Ord_Value(GetString)
    