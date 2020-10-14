import sys
if len(sys.argv)==2:
    if sys.argv[1].isdigit():
        num=int(sys.argv[1])
        print(num**2)
    else:
        print('please enter a number')
elif len(sys.argv)>2:
    print('please enter only one argument(number)')
else:
     print('please enter number')

