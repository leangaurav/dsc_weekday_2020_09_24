# -*- coding: utf-8 -*-
import sys

n1=sys.argv[-1]
n2=sys.argv[-2]
f1 = open(str(n1), 'r')
f2 = open(str(n2), 'r')
print(f1.read()==f2.read())
f1.close()
f2.close()
    