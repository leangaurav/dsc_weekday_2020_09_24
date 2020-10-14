# open file/ get control of a file  => file object
# process file via file object
# close file object
# operations in terms of data: read from, write   (remove, copy, rename...)

# write  : w
# read   : r

try:
    f = open("temp1.txt")
except FileNotFoundError:
    print("Cannot open for reading.. file not present")

f = open("temp.txt", "w")

print(f)
print(dir(f))

f.close()