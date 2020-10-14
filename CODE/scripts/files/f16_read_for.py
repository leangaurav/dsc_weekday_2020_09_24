# for automatically reads line by line
with open("opeartions.csv", "r") as f:
   res = []
   for line in f:
        if line:
            res.append(line.split(","))

print(res)