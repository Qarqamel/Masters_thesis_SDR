import numpy as np
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

NR_OF_SAMPLES           = 7
SIGNAL_FREQUENCY        = 2

time = np.linspace(0, 1, int(10e4))
sine = np.sin(time*2*PI*SIGNAL_FREQUENCY)
sampling_freq = NR_OF_SAMPLES-1
sine_al1 = np.sin(time*2*PI*(SIGNAL_FREQUENCY+sampling_freq))
sine_al2 = np.sin(time*2*PI*(SIGNAL_FREQUENCY+2*sampling_freq))

time_samp = np.linspace(0, 1, NR_OF_SAMPLES)
sine_samp = np.sin(time_samp*2*PI*SIGNAL_FREQUENCY)

my_plot(time, {f'signal ({SIGNAL_FREQUENCY}Hz)':sine})
plt.show()

my_plot(time, {f'alias ({SIGNAL_FREQUENCY+sampling_freq}Hz)':sine_al1})
plt.show()

my_plot(time, {f'alias ({SIGNAL_FREQUENCY+2*sampling_freq}Hz)':sine_al2})
plt.show()

my_plot(time_samp, {f'samples ({sampling_freq}Hz)':sine_samp}, styles=['.'])
plt.show()

my_plot(time, {f'signal ({SIGNAL_FREQUENCY}Hz)':sine,
               f'alias ({SIGNAL_FREQUENCY+sampling_freq}Hz)':sine_al1,
               f'alias ({SIGNAL_FREQUENCY+2*sampling_freq}Hz)':sine_al2},
        [2, 1, 1],
        ['-', '--', '--'])
plt.plot(time_samp, sine_samp, '.', label=f'samples ({sampling_freq}Hz)')
plt.legend(loc = 'lower center', ncol=2, bbox_to_anchor=(0.5, 1))
plt.show()

plt.figure(figsize = [6.4,1], dpi=150, facecolor='#FAF4F6')
ax = plt.axes()
ax.set_facecolor("#FAF4F6")
plt.grid()
plt.plot(time, sine, label=f'signal ({SIGNAL_FREQUENCY}Hz)')
plt.plot(time, sine_al1, label=f'alias ({SIGNAL_FREQUENCY+sampling_freq}Hz)')
plt.plot(time, sine_al2, label=f'alias ({SIGNAL_FREQUENCY+2*sampling_freq}Hz)')
plt.plot(time_samp, sine_samp, '.', label=f'samples ({sampling_freq}Hz)')
plt.legend(loc = 'lower center', ncol=2 , bbox_to_anchor=(0.5, 1))
plt.show()