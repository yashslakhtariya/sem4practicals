from pandas import *
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from matplotlib import *
from YSL_io import *
use('GTK3Agg')

mrks = {
     'E1' : [20, 18, 30, 22, 15],
     'E2' : [19, 22, 33, 30, 19]
}
i = ['FP', 'SE', 'OS', 'FET', 'PS']

frame = df(mrks, index=i)
print()
printGRN(frame)

frame.plot.bar(rot=0, color=['#5e81cc', '#b75969']).set_title('Marks comparison of mid sem exams', fontsize=16)

# Toresize graph window to max in my screen by default on opening it
# m = plt.get_current_fig_manager().resize(1920, 1080)

plt.show()
