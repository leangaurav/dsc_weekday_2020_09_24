with open("test.txt", "r") as f:

    print("Pointer: ", f.tell())
    s = f.read()
    print(repr(s))
    
    # move pointer back to beginning
    f.seek(0)
    print("\n Reading again")
    print("Pointer: ", f.tell())
    s = f.read()
    print(repr(s))
    
print("end")