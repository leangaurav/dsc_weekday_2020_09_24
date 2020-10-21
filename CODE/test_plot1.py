import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

sns.set()

# plot via pandas
s1 = pd.Series(range(10))
print(s1)

print()
s2 = s1**2
print(s2)

plt.subplot(1,2,1)
plt.plot(s1) # alpha => transparency float : [0-1]

plt.subplot(1,2,2)
plt.plot(s2)
plt.show()

