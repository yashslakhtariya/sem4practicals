import numpy as np
from YSL_io import *

plnts = np.array(range(0, 8))
printGRN('\nInitial plants arrangement : ')
print(plnts)

plnts = plnts.reshape(2,4)
printMGNTA('\nAfter equal distribution : ')
print(plnts)

plnts = np.delete(plnts, -1, axis=1)
printORNG('\nAfter 2 plants are destroyed : ')
print(plnts)

plnts = np.append(plnts, [[3],[7]], axis=1)
printBLU('\nFinally adding 2 plants : ')
print(plnts)
