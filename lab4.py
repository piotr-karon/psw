import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
 
np.set_printoptions(precision=3, suppress=True)
 
def interp_nearest(x_source, y_source, x_target):
    idx = np.abs(x_source - x_target[:,None])
    return y_source[idx.argmin(axis=1)]
 
def interp_linear(x_source, y_source, x_target):
    dist = x_source[:, np.newaxis] - x_target[np.newaxis, :]
 
    dist_lower = np.copy(dist)
    dist_lower[dist < 0] = np.NAN
    dist_upper = np.copy(dist)
    dist_upper[dist > 0] = np.NAN
 
    address_lower = np.nanargmin(dist_lower, axis=0)
    address_upper = np.nanargmax(dist_upper, axis=0)
 
    y1 = y_source[address_upper]
    y0 = y_source[address_lower]
 
    x1 = x_source[address_upper]
    x0 = x_source[address_lower]
 
    a = (y1 - y0) / (x1 - x0)
    b = (y0 * x1 - y1 * x0) / (x1 - x0)
 
    result = a * x_target + b;
    result[np.isnan(result)] = y0[np.isnan(result)]
 
    return result
    # return np.zeros_like(x_target)
 
def interp_cubic(x_source, y_source, x_target):
    return np.zeros_like(x_target)
 
# Probers
original_prober = np.sort(np.random.uniform(size=8)*np.pi*4)
target_prober = np.linspace(np.min(original_prober),
                            np.max(original_prober), 32)
 
# Sampling
original_signal = np.sin(original_prober)
 
# Out-of-box interpolators
fn = interp1d(original_prober, original_signal, kind='nearest')
fl = interp1d(original_prober, original_signal, kind='linear')
fc = interp1d(original_prober, original_signal, kind='cubic')
 
# Interpolation
target_signal_fn = fn(target_prober)
target_signal_fl = fl(target_prober)
target_signal_fc = fc(target_prober)
 
args = (original_prober, original_signal, target_prober)
own_target_signal_fn = interp_nearest(*args)
own_target_signal_fl = interp_linear(*args)
own_target_signal_fc = interp_linear(*args)
 
# Store them for plotting
target_signals = [target_signal_fn, target_signal_fl, target_signal_fc]
own_target_signals = [own_target_signal_fn, own_target_signal_fl, own_target_signal_fc]
 
# Plotting
fig, ax = plt.subplots(4,1,figsize=(8, 8*1.618))
 
ax[0].scatter(original_prober, np.ones_like(original_prober) * -.5,
              label = 'origin', c='black')
ax[0].scatter(target_prober, np.ones_like(target_prober) * .5,
              label = 'target', c='red')
ax[0].plot(original_prober, original_signal, c='black')
ax[0].set_ylim(-1.5,1.5)
ax[0].legend(frameon=False, loc=9, ncol=2)
ax[0].set_yticks([])
ax[0].set_xticks(original_prober)
ax[0].set_xticklabels([])
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].grid(ls=":")
 
 
for i, (target_signal, own_target_signal) in enumerate(zip(target_signals,
                                                           own_target_signals)):
    ax[1+i].plot(original_prober, original_signal, c='black', ls=":")
    ax[1+i].plot(target_prober, target_signal, 'red', ls=":")
    ax[1+i].plot(target_prober, own_target_signal, 'red')
    ax[1+i].grid(ls=":")
    ax[1+i].set_xticks(target_prober)
    ax[1+i].set_xticklabels([])
    ax[1+i].spines['top'].set_visible(False)
    ax[1+i].spines['right'].set_visible(False)
 
ax[1].set_title('neighbor')
ax[2].set_title('linear')
ax[3].set_title('cubic')
 
plt.savefig('foo.png')
 