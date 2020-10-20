###Q6. Write a program that take a file name as command line argument, opens it and then counts number of space characters in that file.
import sys
name = sys.argv[1]
f = open(name, 'r')
s = f.read()
print(s.count(' '))
f.close()

###Q6. Write a program that take a file name as command line argument, opens it and then counts number of space characters in that file.
import sys
name = sys.argv[1]
f = open(name, 'r')
s = f.read()

d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

#print(s.count(' '))
print(d)
f.close()