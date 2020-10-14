
# once exexution moves out of with block, file will get closed automatically
with open("temp.txt", "a") as f:
    print(f.closed) # this flag tells if file is closed  or  not
    f.write("\n")
    f.write("This will be appeded")

print(f.closed)