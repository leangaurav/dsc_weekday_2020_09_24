def sumOfDigits(x):
    Sum = 0
    Count = 0
    
    while(Count < len(x)):
        Sum = Sum + int(x[Count:Count+1])
        Count += 1   
    
    return Sum

x = input("Enter Digits:")
if(x.isdigit()):
    print("Sum of Digits:",sumOfDigits(x) )  
else:
    print("Enter only numbers please")


      
        
