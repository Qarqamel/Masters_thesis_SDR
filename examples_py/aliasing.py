import numpy as np
import scipy.signal
from matplotlib import pyplot as plt
from numpy import pi as PI
from auxiliary_lib import my_plot

def lpf(samples, cutoff_freq, sampling_freq):
    b, a = scipy.signal.butter(2, 2*cutoff_freq/sampling_freq, btype='lowpass')
    return scipy.signal.filtfilt(b,a,samples)

NR_OF_SAMPLES           = 7
SIGNAL_FREQUENCY        = 2

time = np.linspace(0, 1, int(10e4))
sine = np.sin(time*2*PI*SIGNAL_FREQUENCY)
sampling_freq = NR_OF_SAMPLES-1
sine_al1 = np.sin(time*2*PI*(SIGNAL_FREQUENCY+sampling_freq))
sine_al2 = np.sin(time*2*PI*(SIGNAL_FREQUENCY+2*sampling_freq))
time_samp = np.linspace(0, 1, NR_OF_SAMPLES)
sine_samp = np.sin(time_samp*2*PI*SIGNAL_FREQUENCY)

my_plot(time, {f'signal ({SIGNAL_FREQUENCY}Hz)':sine,
               f'alias ({SIGNAL_FREQUENCY+sampling_freq}Hz)':sine_al1,
               f'alias ({SIGNAL_FREQUENCY+2*sampling_freq}Hz)':sine_al2},
        [1.5,1,1], leg_ncol=3)
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
