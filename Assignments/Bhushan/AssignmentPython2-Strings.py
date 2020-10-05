AssignmentPython2-Strings
Answers:
1. s="Python is Object Oriented"
s[-1]='d'
s[:-1]='Python is Object Oriente'
s[::-1]=detneirO tcejbO si nohtyP
s[1:1]=''
s[4:10]='on is'

2. Output: String index out of Bound.

3. s not defined. It is case sensitive.

4. 
a. s="a b cd"
print(len(s))--> 6
print(s[::2])--> 'a b c'
print(len(s[::2]))-->5

b. s="a#b#c#d#"
print(s.split())-->['a#b#c#d#']
print(s.split('#'))-->['a', 'b', 'c', 'd', '']
print(l)-->['a', 'b', 'c', 'd', '']
print(s)-->a$b$c$d$

c. s='Gaurav'
print(s[::-2][::-2])-->av

d. print(1>2)-->False

e. print(4%2,5%2,2%5,sep=",")-->0,1,2

f. s='abcba'
s.upper-->ABCBA
print(s.count('A'),end=',')-->2,
print(s.count('A',2,4),end=',')-->0,
print(s.count('a',2,4),end=',')-->0,

5. s='Python is Object Oriented'
z=(s.split(" "))
print(''.join(z))

6. [] denotes either a list or an indexing.

7. print(dir(str))

8. a=dir(str)
if ('rstrip' in a) == 1:
    print("Foundound")
else:
    print("Not Found")
	
9. s='''
*****
  *
  *
  *
  *
  '''
print(s)

10. s='''
*   *
** **
* * *
*   *
*   *
  '''
print(s)

11. s='''
  ____________
  |          |
  o          |
 /|\         |
 / \         |
_____________|
  '''
print(s)

12. s=input("Python is Object Oriented")
print(s.replace(' ',"\n"))

13. s=' Bhushan Basavaraj Pujar '
	s=s.strip()
	print(s)
	z=s.split(" ")
	i=0
	print(i)
	if s.find(" ")!=-1:
		while (i<len(z)):
			print(z[i].upper(),len(z[i]),sep=' ')
			i=i+1
	else: 
		print("Error: Enter Name and First name seperated by space")
		
14. s="BhushanPuja"
x=len(s)
print(z)
if(z%2==0):
    s1=s[:z//2+1]
    s2=s[z//2+1::]
    print(s1)
    print(s2)
else:
    z=z+1
    s1=s[:z//2+1]
    s2=s[z//2+1::]
    print(s1)
    print(s2)
	
