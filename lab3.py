import numpy as np
import math
import matplotlib.pyplot as plt
import copy

resolution = 256
depth = 2
drange = (-1, 1)
n_iter = 256
N = np.power(2, depth) - 1
prober = np.linspace(0, 8 * math.pi, resolution)
prober = np.sin(prober)
perfect_image = np.outer(prober, prober)
n_matrix = np.zeros(perfect_image.shape)
o_matrix = np.zeros(perfect_image.shape)

for i in range(n_iter):
    noise = np.random.normal(size=perfect_image.shape)

    #n_image
    n_image = perfect_image + noise
    n_image = (n_image - drange[0]) / (drange[1] - drange[0])
    n_image = np.clip(n_image, 0, 1)
    n_dimg = np.rint(n_image * N)
    n_matrix = n_matrix + n_dimg

    #o_image
    o_image = copy.deepcopy(perfect_image)
    o_image = (o_image - drange[0]) / (drange[1] - drange[0])
    o_image = np.clip(o_image, 0, 1)
    o_dimg = np.rint(o_image * N)
    o_matrix = o_matrix + o_dimg

    # Prepare plots
    fig, ax = plt.subplots(2, 3, figsize=(12, 8))
    ax[0,0].imshow(perfect_image, cmap='binary')
    ax[1,0].imshow(noise, cmap='binary')
    ax[0,1].imshow(o_dimg, cmap='binary')
    ax[1,1].imshow(n_dimg, cmap='binary')
    ax[0,2].imshow(o_matrix, cmap='binary')
    ax[1,2].imshow(n_matrix, cmap='binary')

    # Save it to file
    print(f'Saving iteration number: "{i}"')
    file_name = f'iter/iter-{i}.png'
    plt.tight_layout()
    plt.savefig(file_name)
