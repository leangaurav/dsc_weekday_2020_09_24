import sys
if(len(sys.argv)== 1):
        print("give a number")
else:
        if(len(sys.argv) > 2):
                print ("only one arg")
        else:
                print(int(sys.argv[1])**2)