from matplotlib import pyplot as plt
import numpy as np
import random
import json

points=np.random.choice(range(100), size=(10000,2))

path1='./points.txt'

with open(path1,'w') as file:
    file.write(' '.join([str(x) for x in points.flat]))

plt.scatter(*zip(*points))
plt.grid()
# plt.pause(5)
# plt.close()
plt.show()

