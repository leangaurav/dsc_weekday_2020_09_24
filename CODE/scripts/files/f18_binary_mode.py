# binary mode returns bytes
with open("opeartions.csv", "rb") as f:
   data = f.read()
   print(type(data), len(data))