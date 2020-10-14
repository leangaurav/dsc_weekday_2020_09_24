with open("test.txt", "r") as f:

    print("Pointer: ", f.tell())
    s = f.read()
    print(repr(s))
    
    print("\n Reading again")
    print("Pointer: ", f.tell())
    s = f.read()
    print(repr(s))
    
print("end")