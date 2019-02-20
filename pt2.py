import numpy as np
import pylab as plt
from skfmm import distance, travel_time

from skimage import io

img=io.imread("path11545.png")

data = img[:,:,3].astype(np.double)
data = (data-data.max()/2.0)/data.max()

dist = distance(data)

plt.contour(dist,20, colors="black", linewidths=0.5, linestyles="solid")
plt.contour(dist,[0], colors="black", linewidths=3)
plt.gca().set_aspect(1)


plt.xticks([])
plt.yticks([])
#plt.gca().set_frame_on(False)

plt.show()


sfunc = np.zeros_like(data)
for (i,j), v in np.ndenumerate(data):
    sfunc[i,j] = 0.25+j/data.shape[1] * 2.0

dist = travel_time(data, sfunc)
plt.contour(dist,20, colors="black", linewidths=0.5, linestyles="solid")
plt.contour(data,[0], colors="black", linewidths=3)
plt.gca().set_aspect(1)


plt.xticks([])
plt.yticks([])
#plt.gca().set_frame_on(False)

plt.show()
