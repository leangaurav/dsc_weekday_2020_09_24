with open("test.txt", "r") as f:

    print("Pointer: ", f.tell())
    s = f.read(5) # read 5 bytes
    print(repr(s))
    
    print("\n Reading again")
    print("Pointer: ", f.tell())
    s = f.read()
    print(repr(s))
    
print("end")