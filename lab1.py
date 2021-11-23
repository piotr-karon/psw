import numpy as np
import math
import matplotlib.pyplot as plt
 
resolution = 32
depth = 8
 
x = np.linspace(0, 4 * math.pi, resolution)
matr = np.zeros((16, 16))
 
fig, ax = plt.subplots(2, 3, figsize=(10, 5))
 
top_left = ax[0][0]
top_left.plot(x)
 
matr[6:10, 6:10] = 5
 
bottom_right = ax[1][2]
bottom_right.imshow(matr, cmap='viridis', interpolation='none')
 
space = np.linspace(0, 10, 30)
sinner = np.sin(space)
 
ax[0, 1].plot(space, sinner, c='red', label="")
ax[0, 1].grid(ls=":")
ax[0, 1].spines['top'].set_visible(False)
ax[0, 1].spines['right'].set_visible(False)
ax[0, 1].set_xlabel('os X')
ax[0, 1].set_ylabel("os Y")
ax[0, 1].legend()
 
reflectance = np.sin(x)
image = reflectance[:, np.newaxis] * reflectance[np.newaxis, :]
 
nrange = (-1, 1)
norm_image = (image - nrange[0]) / (nrange[1] - nrange[0])
norm_image = np.clip(norm_image, 0, 1)
 
dmin, dmax = (0, np.power(2, depth) - 1)
dig_image = np.rint(norm_image * dmax)
 
ax[1][0].imshow(image, cmap='binary', vmin=0, vmax=1)
ax[1][1].imshow(norm_image, cmap='binary', vmin=0, vmax=1)
ax[0][2].imshow(dig_image, cmap='binary', vmin=0, vmax=dmax)
 
plt.tight_layout()
plt.savefig('foo.png')