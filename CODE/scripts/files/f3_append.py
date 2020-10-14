# opening a file in append mode
# - if file  exists move file pointer to end of file
# - if  file doesn't exist create it
f = open("temp.txt", "a")

# write takes a string as argumet and wirtes to file
f.write("\n")
f.write("This will be appeded")

f.close()