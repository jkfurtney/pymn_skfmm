import numpy as np
import pylab as plt
#from skfmm import distance, travel_time

from skimage import io

img = io.imread("raw_wells.png")

data = img[:,:,3].astype(np.double)
data = (data-data.max()/2.0)/data.max()
np.save("rw.npy",data)
dist = -np.load("well_out.npy")

X, Y = np.meshgrid(np.linspace(0,2000,2000), np.linspace(0,3100,3100))

#plt.contour(X,Y,dist,[100,200,300,400],colors=["black"])
c=0
for i in range(1,300,3):
    print(i)
    plt.cla()
    plt.contourf(X,Y,dist,[i,1e6],colors=["brown"])
    plt.gca().set_aspect(1.0)
    plt.savefig("frame{:03d}.png".format(c))
    c += 1
