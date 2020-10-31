import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# plot via pandas
s1 = pd.Series(range(10))
print(s1)

print()
s2 = s1**2
print(s2)

plt.plot(s1,c='r',alpha=0.5) # alpha => transparency float : [0-1]
plt.plot(s2)
plt.show()