import numpy as np
import pylab as plt

t = np.linspace(0,10,100)
v = 1-np.exp(-t*0.75)

print(v)
plt.plot(t,v, linewidth=3)
plt.xlabel("Time in hours", fontsize=20)
plt.ylabel("Brine concentration", fontsize=20)
plt.show()
