with open("test.txt", "w") as f:
    print(f.tell())
    f.write("abcd")
    print(f.tell()) # position of file pointer
    f.write("another line")
    print(f.tell())
 
print("end")