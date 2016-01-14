import numpy as np
import pylab as plt
from skfmm import distance

from skimage import io

img=io.imread("rect3013.png")

data = img[:,:,0].astype(np.double)
data = (data-data.max()/2.0)/data.max()

dist = distance(data)
plt.contour(dist,20, colors="black", linestyles="solid")
plt.contour(dist,[0], colors="black", linewidths=3)
plt.gca().set_aspect(1)


plt.xticks([])
plt.yticks([])
#plt.gca().set_frame_on(False)

plt.show()
