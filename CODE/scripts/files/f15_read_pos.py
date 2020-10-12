with open("opeartions.csv", "r") as f:
    lines = f.read().split("\n")
    res = []
    for line in lines:
        if line:
            res.append(line.split(","))

print(res)