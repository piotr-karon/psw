import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import rectangle
from skimage.transform import rotate
from scipy.signal import convolve2d, medfilt
 
entry_img = np.zeros((256, 256))
 
entry_img[rectangle((32, 32), (92, 92))] = 1.0
entry_img[rectangle((92, 92), (128, 128))] = 1.0
entry_img[rectangle((128, 128), (144, 144))] = 1.0
 
angle = np.random.randint(-20, 20, 1)[0]
 
rot_img = rotate(image=entry_img, angle=angle)
 
S1 = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
S3 = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
 
angles = np.linspace(-30, 30, 50)
 
abssums_s1 = np.zeros(50)
abssums_s3 = np.zeros(50)
 
fig, x = plt.subplots(3, 2)
x[0, 0].imshow(entry_img)
x[0, 1].imshow(rot_img)
 
for i, ang in enumerate(angles):
    out_img = rotate(rot_img, ang)
    conv_s1 = convolve2d(out_img, S1)
    conv_s3 = convolve2d(out_img, S3)
 
    x[1, 0].imshow(out_img)
    x[1, 1].imshow(conv_s1)
    x[2, 1].imshow(conv_s3)
 
    abssums_s1[i] = np.abs(conv_s1).sum()
    abssums_s3[i] = np.abs(conv_s3).sum()
 
    # plt.pause(0.01)
 
x[2, 0].clear()
x[2, 0].plot(angles, abssums_s1)
x[2, 0].plot(angles, abssums_s3)
 
best_angle_s1 = angles[np.argmin(abssums_s1)]
best_angle_s3 = angles[np.argmin(abssums_s3)]
 
best_angle = (best_angle_s1 / best_angle_s3) / 2.0
 
final_img = rotate(rot_img, best_angle)
 
plt.imsave("baz.png", final_img)
 
bar = np.zeros((256, 256, 3))
bar[:, :, 0] = entry_img
bar[:, :, 1] = final_img
bar[:, :, 2] = rot_img
 
plt.imsave("baz.png", final_img)
plt.imsave("bar.png", bar)
print(best_angle)
plt.show()
 