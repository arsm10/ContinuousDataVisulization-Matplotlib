import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    scat=plt.scatter(i, y)
    
    #Delay
    plt.pause(1)
    #scat.remove()

plt.show()
