import sys

if len(sys.argv) != 3:
    print("Invalid input")
    exit()

name1 = sys.argv[1]
name2 = sys.argv[2]

#  with keyword.. for context management

with open(name1, "r") as  f1:
    s  = f1.read()
    with open(name2, "w") as f2:
        f2.write(s)
        
    print(f1.closed, f2.closed)

print(f1.closed, f2.closed)