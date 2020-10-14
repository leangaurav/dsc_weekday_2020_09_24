while True:
    s=input("Enter data:")
    f=open("dump.txt","w")
    if s.strip()=='':
        f.close()
        break
    else:
        f.write(s)
