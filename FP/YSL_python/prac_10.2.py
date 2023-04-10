import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
use('GTK3Agg')

y = random.randint(0, 30)
x = 40 - y
X = 30 - y

t = np.array([6, x, 46, y, 8])
p = np.array([10, 28, X, y, 32])

mrks = ['0-20', '20-40', '40-60', '60-80', '80-100']

plt.bar(x=mrks, height=p, color='#b75969')
plt.title('Practical Marks of students')
plt.xlabel('Range')
plt.ylabel('Number of students')
plt.show()
