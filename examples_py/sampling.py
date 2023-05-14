import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt

SIGNAL_FREQUENCY        = 20
SAMPLING_FREQUENCY      = 10

time_original = np.linspace(0, 1, 1000)
sinewave_original = np.sin(time_original*2*PI*SIGNAL_FREQUENCY)

time = np.linspace(0, 1, SAMPLING_FREQUENCY)
sinewave = np.sin(time*2*PI*SIGNAL_FREQUENCY)

fig, axs = plt.subplots(3, dpi=150)
fig.suptitle('Signal sampling', fontsize = 12)
axs[-1].set_xlabel('time [s]')

axs[0].grid()
axs[0].set_title(f'signal frequency = {SIGNAL_FREQUENCY}', fontsize = 8)
axs[0].plot(time_original, sinewave_original, '-', label = 'Original signal')

axs[1].grid()
axs[1].set_title(f'sampling frequency = {SAMPLING_FREQUENCY}', fontsize = 8)
axs[1].plot(time, sinewave, '.', color = 'orange', label = 'Sampled signal')

axs[2].grid()
axs[2].plot(time_original, sinewave_original, '-')
axs[2].plot(time, sinewave, '.', color = 'orange')

fig.legend()
fig.tight_layout()
fig.show()
