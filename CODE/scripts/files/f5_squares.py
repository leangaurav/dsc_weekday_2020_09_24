f = open("opeartions.csv", "w")

op = {"add": lambda x,y: x + y, "sub": lambda x,y: x - y, "mul": lambda x,y: x * y}

import random

ops = list(op.keys())  # add, sub, mul
for x, y in zip(range(10), range(100,110)): # 0,100  1,101  2,102
    o = ops[random.randrange(len(ops))]
    print(o, x, y, op[o](x,y), file=f, sep=",")

f.close()