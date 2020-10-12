# opening a file in write mode
# - if file  exists clear its contents
# - if  file doesn't exist create it
f = open("temp.txt", "w")

# write takes a string as argumet and wirtes to file
f.write("Python programming language")
f.write("\n")
f.write("This will be appeded")



f.close()