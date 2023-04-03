import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('GTK3Agg')

values = np.array([5,8,9,4,1,6,7,2,3,8])
f1 = plt.figure(1)
plt.plot(range(1,11), values, c='#b75969', ls='--', marker='*')
# plt.show()

values2= [305, 436, 805, 35, 512, 640]
l = np.array(['Service', 'Reading', 'Chanting', 'Trip', 'Prasadam', 'Kirtan'])
c = np.array(['#5e81cc', '#2aa1b3', '#BF616C', '#d18677', '#a347ba', '#eaca8a'])
e = np.array([0, 0.22, 0, 0, 0, 0])
f2 = plt.figure(2)
plt.pie(values2, colors=c, labels=l, explode=e, autopct='%1.3f%%')
plt.legend()
# plt.show()

x = np.array([1,2,3,4,5])
y = np.array([8.7, 9.3, 9.2, 9.9, 9.5])
c = np.array(['#5e81cc', '#2aa1b3', '#BF616C', '#eaca8a', '#a347ba'])
l = np.array(['Sem1', 'Sem2', 'Sem3', 'Sem4', 'Sem5'])
w = np.array([0.5, 0.6, 1.2, 0.5, 0.9])
f3 = plt.figure(3)
plt.bar(x, y, label=l, width=w, color=c)
plt.title('Sem-wise Score')
plt.legend()
plt.show()