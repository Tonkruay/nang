#import numpy as np

#x = np.array

#location = ((1,2,3),(4,5,6))
#print(type(location))
#print(location[1])
#print(tuple(zip(location)))
#print(list(zip(*location[::-1])))

import numpy as np

x = np.array([1,2,3,4,5])
y = np.where(x>3,1,0)
y1 = np.where(x>3)
print(y)
print(y1)