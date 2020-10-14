f=open("sample_file_usrer.txt","w")
while True:
    str1=input("Enter a string: ")
    if str1=='':
        break
    else:
        f.write(str1)
        f.write('\n')

f.close()