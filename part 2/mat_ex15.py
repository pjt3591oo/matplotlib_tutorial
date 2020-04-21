import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# img = mpimg.imread('mung.png')
# plt.imshow(img)
# plt.axis('off')
# plt.show()

# img = np.arange(100*100).reshape(100, 100)
# print(img)
# plt.imshow(img, cmap="hot")
# plt.show()

img = np.empty((20,30,3))
img[:, :10] = [0, 0, 0.6]
img[:, 10:20] = [1, 1, 1]
img[:, 20:] = [0.6, 0, 0]
plt.imshow(img, interpolation="nearest")
plt.show()